/*
 * Dependency graph views for the book.
 *
 * Reads graph.json (built by Jekyll from the links between D/ and T/ pages)
 * and draws it with Cytoscape.js + dagre, prerequisites above the pages
 * that use them. Two views:
 *
 *   <div data-book-graph="full" data-graph-url="..."></div>
 *       the whole book, with search, chapter filter and click-to-highlight
 *
 *   <details data-book-graph="page" data-graph-url="..." data-focus="D/slug">
 *       one page's prerequisites (2 levels, or all) and direct dependents;
 *       libraries load only when the reader opens it
 *
 *   <div data-book-graph="feature" data-graph-url="..." data-focus="T/slug">
 *       the home page teaser: a page's graph as its own panel first shows it
 *
 * An edge in graph.json goes source -> target meaning "source uses target";
 * drawn edges point the other way, from prerequisite down to user.
 */
(function () {
  "use strict";

  var LIBS = [
    ["https://cdnjs.cloudflare.com/ajax/libs/cytoscape/3.30.2/cytoscape.min.js",
     "sha384-IWROdLKRsN1UuJywMlWl7/blXQ8GEooN2n7dzTxfEPd7ybYIKCUJ2Ol/1Gpf3YV4"],
    ["https://cdnjs.cloudflare.com/ajax/libs/dagre/0.8.5/dagre.min.js",
     "sha384-2IH3T69EIKYC4c+RXZifZRvaH5SRUdacJW7j6HtE5rQbvLhKKdawxq6vpIzJ7j9M"],
    ["https://cdn.jsdelivr.net/npm/cytoscape-dagre@2.5.0/cytoscape-dagre.js",
     "sha384-u69h9ebXeSjlg6q/rb1zKTRAGu/h8deCl0409xpS/QJctMKnc4M9Fzkm01VOQdeF"]
  ];

  // ---------- loading ----------

  var libsPromise = null;
  function loadLibs() {
    if (!libsPromise) {
      libsPromise = LIBS.reduce(function (chain, lib) {
        return chain.then(function () {
          return new Promise(function (resolve, reject) {
            var s = document.createElement("script");
            s.src = lib[0];
            s.integrity = lib[1];
            s.crossOrigin = "anonymous";
            s.onload = resolve;
            s.onerror = function () { reject(new Error("Could not load " + lib[0])); };
            document.head.appendChild(s);
          });
        });
      }, Promise.resolve());
    }
    return libsPromise;
  }

  var dataPromises = {};
  function loadGraph(url) {
    if (!dataPromises[url]) {
      dataPromises[url] = fetch(url).then(function (r) {
        if (!r.ok) throw new Error("Could not load " + url);
        return r.json();
      }).then(indexGraph);
    }
    return dataPromises[url];
  }

  function indexGraph(g) {
    var byId = {}, uses = {}, usedBy = {};
    g.nodes.forEach(function (n) { byId[n.id] = n; uses[n.id] = []; usedBy[n.id] = []; });
    g.edges.forEach(function (e) {
      if (!byId[e.source] || !byId[e.target]) return;
      uses[e.source].push(e.target);
      usedBy[e.target].push(e.source);
    });
    return { nodes: g.nodes, edges: g.edges, byId: byId, uses: uses, usedBy: usedBy };
  }

  // Nodes reachable from `start` along `adj`, mapped to their distance.
  function reach(adj, start, maxDepth) {
    var dist = {}, frontier = [start], d = 0;
    while (frontier.length && d < maxDepth) {
      d += 1;
      var next = [];
      frontier.forEach(function (v) {
        adj[v].forEach(function (w) {
          if (w !== start && !(w in dist)) { dist[w] = d; next.push(w); }
        });
      });
      frontier = next;
    }
    return dist;
  }

  // ---------- drawing ----------

  function token(el, name) {
    return getComputedStyle(el).getPropertyValue(name).trim();
  }

  // Transitive reduction of the drawn pages: if A -> B -> C and also
  // A -> C, the shortcut A -> C is "implied" and not drawn by default.
  // Reachability is unchanged, so "what do I need first?" reads the same.
  // Computed per view, against only the pages being drawn: a shortcut stays
  // when the longer path runs through a page the view leaves out.
  function reduce(graph, ids) {
    var keep = {}, uses = {}, usedBy = {}, implied = [];
    ids.forEach(function (id) { keep[id] = true; uses[id] = []; usedBy[id] = []; });
    ids.forEach(function (s) {
      var direct = graph.uses[s].filter(function (t) { return keep[t]; });
      // Pages reachable from s in two or more steps (never back through s).
      var far = {}, stack = [];
      direct.forEach(function (c) { stack = stack.concat(graph.uses[c]); });
      while (stack.length) {
        var v = stack.pop();
        if (!keep[v] || v === s || far[v]) continue;
        far[v] = true;
        stack = stack.concat(graph.uses[v]);
      }
      direct.forEach(function (t) {
        if (far[t]) { implied.push([s, t]); }
        else { uses[s].push(t); usedBy[t].push(s); }
      });
    });
    return { byId: graph.byId, uses: uses, usedBy: usedBy, implied: implied };
  }

  function elementsFor(reduced, ids) {
    var els = ids.map(function (id) {
      var n = reduced.byId[id];
      return { group: "nodes", data: { id: id, label: n.title, url: n.url, chapter: n.chapter },
               classes: n.kind };
    });
    function edge(s, t, cls) {
      // Drawn from prerequisite (t) down to the page that uses it (s).
      els.push({ group: "edges", data: { id: t + ">" + s, source: t, target: s }, classes: cls });
    }
    ids.forEach(function (s) { reduced.uses[s].forEach(function (t) { edge(s, t, ""); }); });
    reduced.implied.forEach(function (e) { edge(e[0], e[1], "implied"); });
    return els;
  }

  function style(el) {
    var t = function (n) { return token(el, n); };
    return [
      { selector: "node", style: {
          "shape": "round-rectangle",
          "width": 160, "height": 50,
          "label": "data(label)",
          "text-wrap": "wrap", "text-max-width": 146,
          "text-valign": "center", "text-halign": "center",
          "font-family": t("--graph-font"), "font-size": 12,
          "color": t("--graph-ink"),
          "border-width": 2,
          "min-zoomed-font-size": 6
      } },
      // Same convention as the ToC: definitions italic, theorems bold.
      { selector: "node.definition", style: {
          "background-color": t("--graph-definition-fill"),
          "border-color": t("--graph-definition"),
          "font-style": "italic"
      } },
      { selector: "node.theorem", style: {
          "background-color": t("--graph-theorem-fill"),
          "border-color": t("--graph-theorem"),
          "font-weight": "bold"
      } },
      { selector: "node.focus", style: {
          "border-width": 3.5, "border-color": t("--graph-ink"), "font-size": 13
      } },
      { selector: "node.context", style: { "border-style": "dashed", "opacity": 0.75 } },
      { selector: "edge", style: {
          "width": 1.25,
          "line-color": t("--graph-edge"),
          "target-arrow-color": t("--graph-edge"),
          "target-arrow-shape": "triangle", "arrow-scale": 0.8,
          "curve-style": "bezier"
      } },
      { selector: "edge.highlight", style: {
          "width": 2,
          "line-color": t("--graph-edge-strong"),
          "target-arrow-color": t("--graph-edge-strong"),
          "z-index": 10
      } },
      { selector: ".faded", style: { "opacity": 0.12 } },
      // Shortcut edges: hidden until their page is selected in the full
      // graph, then dashed.
      { selector: "edge.implied", style: { "display": "none" } },
      { selector: "edge.implied.shown", style: {
          "display": "element",
          "line-style": "dashed", "line-dash-pattern": [5, 4],
          "width": 1.5,
          "line-color": t("--graph-edge-strong"),
          "target-arrow-color": t("--graph-edge-strong"),
          "opacity": 1, "z-index": 9
      } },
      { selector: "node:active", style: { "overlay-opacity": 0.08 } }
    ];
  }

  // Layered layout for the full book. Each page sits one row below its
  // deepest prerequisite (dagre's rankers instead pile every unused theorem
  // into one very wide bottom row), and pages with no prerequisites sit just
  // above their first use. Rows start grouped by chapter, then a
  // few barycenter sweeps pull connected pages together to cut crossings.
  function layeredPositions(graph, ids) {
    var inSet = {}, rank = {}, rows = [], pos = {};
    ids.forEach(function (id) { inSet[id] = true; });
    function rankOf(id, stack) {
      if (id in rank) return rank[id];
      stack[id] = true;
      var r = 0;
      graph.uses[id].forEach(function (u) {
        if (inSet[u] && !stack[u]) r = Math.max(r, rankOf(u, stack) + 1);
      });
      delete stack[id];
      return (rank[id] = r);
    }
    ids.forEach(function (id) { rankOf(id, {}); });
    // A page with no prerequisites would otherwise sit in the top row however
    // late it is first used; put it just above its earliest user instead, so
    // the top row doesn't fill with every basic definition in the book.
    ids.forEach(function (id) {
      if (rank[id] !== 0) return;
      var users = graph.usedBy[id].filter(function (u) { return inSet[u]; });
      if (users.length) {
        rank[id] = Math.min.apply(null, users.map(function (u) { return rank[u]; })) - 1;
      }
    });
    ids.forEach(function (id) { (rows[rank[id]] = rows[rank[id]] || []).push(id); });
    rows = rows.filter(Boolean);
    rows.forEach(function (row) {
      row.sort(function (a, b) {
        var na = graph.byId[a], nb = graph.byId[b];
        return na.chapter.localeCompare(nb.chapter) || na.title.localeCompare(nb.title);
      });
    });

    function place() { rows.forEach(function (row) { row.forEach(function (id, i) { pos[id] = i - (row.length - 1) / 2; }); }); }
    function sweep(row, neighbors) {
      var bary = {};
      row.forEach(function (id) {
        var ns = neighbors[id].filter(function (n) { return inSet[n]; });
        bary[id] = ns.length
          ? ns.reduce(function (sum, n) { return sum + pos[n]; }, 0) / ns.length
          : pos[id];
      });
      row.sort(function (a, b) { return bary[a] - bary[b]; });
    }
    place();
    for (var pass = 0; pass < 6; pass++) {
      for (var i = 1; i < rows.length; i++) { sweep(rows[i], graph.uses); place(); }
      for (var j = rows.length - 2; j >= 0; j--) { sweep(rows[j], graph.usedBy); place(); }
    }

    var out = {};
    rows.forEach(function (row, r) {
      row.forEach(function (id) { out[id] = { x: pos[id] * 178, y: r * 110 }; });
    });
    return out;
  }

  // opts.layered: row layout (otherwise dagre); opts.fixed: no zooming or
  // panning, so a graph inside an article never captures the reader's
  // scroll wheel or touch scrolling.
  function draw(container, graph, ids, focusId, opts) {
    var reduced = reduce(graph, ids);
    var cy = cytoscape({
      container: container,
      elements: elementsFor(reduced, ids),
      style: style(container),
      layout: { name: "preset" },
      minZoom: 0.1, maxZoom: 2.5,
      wheelSensitivity: 0.3,
      boxSelectionEnabled: false,
      userZoomingEnabled: !opts.fixed,
      userPanningEnabled: !opts.fixed,
      autoungrabify: true
    });
    // Lay out using the drawn (reduced) edges only.
    cy.elements().not(".implied").layout(opts.layered
      ? { name: "preset", positions: layeredPositions(reduced, ids), padding: 16 }
      : { name: "dagre", rankDir: "TB", nodeSep: 18, rankSep: 46, edgeSep: 6,
          ranker: "network-simplex", padding: 16 }).run();
    if (focusId) cy.getElementById(focusId).addClass("focus");
    return cy;
  }

  function showError(el, err) {
    el.textContent = "The graph could not be loaded (" + err.message + ").";
    el.classList.add("book-graph-error");
  }

  // A small tooltip naming the hovered node; labels are unreadable when zoomed out.
  function addTooltip(cy, wrap, graph) {
    var old = wrap.querySelector(".book-graph-tip");
    if (old) old.remove();
    var tip = document.createElement("div");
    tip.className = "book-graph-tip";
    tip.hidden = true;
    wrap.appendChild(tip);
    cy.on("mouseover", "node", function (evt) {
      var n = graph.byId[evt.target.id()];
      tip.textContent = "";
      var title = document.createElement("strong");
      title.textContent = n.title;
      var meta = document.createElement("span");
      meta.textContent = (n.kind === "definition" ? "Definition" : "Theorem") + " · " + n.chapter;
      tip.appendChild(title);
      tip.appendChild(meta);
      var p = evt.target.renderedPosition();
      tip.style.left = p.x + "px";
      tip.style.top = (p.y - evt.target.renderedHeight() / 2 - 8) + "px";
      tip.hidden = false;
      wrap.style.cursor = "pointer";
    });
    cy.on("mouseout", "node", function () { tip.hidden = true; wrap.style.cursor = ""; });
    cy.on("viewport", function () { tip.hidden = true; });
  }

  function legend(withDashed) {
    var box = document.createElement("div");
    box.className = "book-graph-legend";
    [["definition", "Definition"], ["theorem", "Theorem"]].forEach(function (k) {
      var item = document.createElement("span");
      var swatch = document.createElement("span");
      swatch.className = "book-graph-swatch " + k[0];
      item.appendChild(swatch);
      item.appendChild(document.createTextNode(k[1]));
      box.appendChild(item);
    });
    if (withDashed) {
      var dashed = document.createElement("span");
      var line = document.createElement("span");
      line.className = "book-graph-swatch-dashed";
      dashed.appendChild(line);
      dashed.appendChild(document.createTextNode("Direct link also implied by a longer path"));
      box.appendChild(dashed);
    }
    var arrow = document.createElement("span");
    arrow.textContent = "Arrows point from a prerequisite to the page that uses it";
    arrow.className = "book-graph-hint";
    box.appendChild(arrow);
    return box;
  }

  // ---------- one page and its surroundings ----------

  // Draws `ids` around `focus` in a column-width canvas that doesn't zoom or
  // pan, with `downs` (pages that use the focus) dashed as context. Clicking
  // a box opens that page; the focus itself only when `linkFocus` is set.
  function drawFocused(wrap, graph, focus, ids, downs, linkFocus) {
    wrap.textContent = "";
    // Shortcut edges stay hidden here: drawn straight, they would cut
    // through the boxes in a narrow column.
    var cy = draw(wrap, graph, ids, focus, { layered: ids.length > 12, fixed: true });
    downs.forEach(function (d) { cy.getElementById(d).addClass("context"); });
    // Size the canvas to the laid-out graph: as wide as the column
    // allows (never above 100%), then just tall enough, within limits.
    var bb = cy.elements().boundingBox();
    var scale = Math.min(1, (wrap.clientWidth - 32) / bb.w);
    wrap.style.height = Math.round(Math.min(640, Math.max(200, bb.h * scale + 32))) + "px";
    cy.resize();
    cy.fit(undefined, 16);
    if (cy.zoom() > 1) { cy.zoom(1); cy.center(); }
    cy.on("tap", "node", function (evt) {
      if (linkFocus || evt.target.id() !== focus) window.location.href = evt.target.data("url");
    });
    addTooltip(cy, wrap, graph);
    return cy;
  }

  // The pages a per-page graph shows: prerequisites up to `depth` levels
  // back, plus the pages that use the focus directly unless there are more
  // than MAX_DEPENDENTS (a much-used definition has dozens).
  var MAX_DEPENDENTS = 8;
  function focusedIds(graph, focus, depth) {
    var ups = Object.keys(reach(graph.uses, focus, depth));
    var allDowns = graph.usedBy[focus];
    var downs = allDowns.length <= MAX_DEPENDENTS
      ? allDowns.filter(function (d) { return ups.indexOf(d) < 0; })
      : [];
    return { ids: [focus].concat(ups, downs), downs: downs, allDowns: allDowns };
  }

  // ---------- home page feature ----------

  // One page's graph exactly as its own "Prerequisite graph" panel first
  // shows it: a taste of the full graph.
  function featureView(root) {
    var url = root.getAttribute("data-graph-url");
    var focus = root.getAttribute("data-focus");
    var wrap = root.querySelector(".book-graph-canvas");
    var legendBox = root.querySelector("[data-graph-legend]");
    if (legendBox) legendBox.appendChild(legend(false));
    wrap.textContent = "Loading…";

    Promise.all([loadGraph(url), loadLibs()]).then(function (res) {
      var graph = res[0];
      if (!graph.byId[focus]) { wrap.textContent = ""; root.hidden = true; return; }
      var shown = focusedIds(graph, focus, 2);
      drawFocused(wrap, graph, focus, shown.ids, shown.downs, true);
    }).catch(function (err) { showError(wrap, err); });
  }

  // ---------- per-page view ----------

  function pageView(details) {
    var url = details.getAttribute("data-graph-url");
    var focus = details.getAttribute("data-focus");
    var body = details.querySelector(".book-graph-body");
    var started = false;

    function start() {
      if (!details.open || started) return;
      started = true;
      body.textContent = "Loading…";

      Promise.all([loadGraph(url), loadLibs()]).then(function (res) {
        var graph = res[0];
        if (!graph.byId[focus]) { body.textContent = "This page is not in the graph yet."; return; }
        body.textContent = "";

        var controls = document.createElement("div");
        controls.className = "book-graph-controls";
        var allDepth = Object.keys(reach(graph.uses, focus, Infinity)).length;
        var twoDepth = Object.keys(reach(graph.uses, focus, 2)).length;
        // Past this many, a column-width drawing is unreadable; the full graph
        // (same pages highlighted, at full width) is the better view.
        var MAX_ALL = 25;
        var toggle = null;
        if (allDepth > twoDepth && allDepth <= MAX_ALL) {
          toggle = document.createElement("button");
          toggle.type = "button";
          controls.appendChild(toggle);
        }
        controls.appendChild(legend(false));
        var full = document.createElement("a");
        full.href = details.getAttribute("data-full-url") + "#" + focus;
        full.textContent = allDepth > MAX_ALL
          ? "See all " + allDepth + " prerequisites in the full graph"
          : "Open in the full graph";
        controls.appendChild(full);
        body.appendChild(controls);

        var wrap = document.createElement("div");
        wrap.className = "book-graph-canvas book-graph-canvas-page";
        body.appendChild(wrap);

        var allDowns = graph.usedBy[focus];
        if (allDowns.length > MAX_DEPENDENTS) {
          var note = document.createElement("p");
          note.className = "book-graph-note";
          note.textContent = allDowns.length + " pages build on this one; they are listed under " +
                             "\u201cUsed in\u201d above and shown in the full graph.";
          body.insertBefore(note, wrap);
        }

        var depth = 2, cy = null;
        function render() {
          var shown = focusedIds(graph, focus, depth);
          var ids = shown.ids;
          if (ids.length === 1) {
            wrap.textContent = "This page has no prerequisites or dependents yet.";
            return;
          }
          if (toggle) {
            toggle.textContent = depth === 2
              ? "Show all " + allDepth + " prerequisites"
              : "Show nearest prerequisites only";
          }
          if (cy) cy.destroy();
          cy = drawFocused(wrap, graph, focus, ids, shown.downs, false);
        }
        if (toggle) {
          toggle.addEventListener("click", function () {
            depth = depth === 2 ? Infinity : 2;
            render();
          });
        }
        render();
      }).catch(function (err) { showError(body, err); });
    }
    details.addEventListener("toggle", start);
    start();
  }

  // ---------- full-book view ----------

  function fullView(root) {
    var url = root.getAttribute("data-graph-url");
    var canvas = root.querySelector(".book-graph-canvas");
    var search = root.querySelector("[data-graph-search]");
    var chapterSelect = root.querySelector("[data-graph-chapter]");
    var reset = root.querySelector("[data-graph-reset]");
    var info = root.querySelector("[data-graph-info]");
    var options = root.querySelector("#book-graph-titles");
    root.querySelector("[data-graph-legend]").appendChild(legend(true));
    canvas.textContent = "Loading…";

    Promise.all([loadGraph(url), loadLibs()]).then(function (res) {
      var graph = res[0], cy = null, titleToId = {}, view = {};
      canvas.textContent = "";

      var chapters = [];
      graph.nodes.forEach(function (n) {
        if (chapters.indexOf(n.chapter) < 0) chapters.push(n.chapter);
        titleToId[n.title.toLowerCase()] = n.id;
        var opt = document.createElement("option");
        opt.value = n.title;
        options.appendChild(opt);
      });
      chapters.sort().forEach(function (c) {
        var opt = document.createElement("option");
        opt.value = c;
        opt.textContent = c;
        chapterSelect.appendChild(opt);
      });

      function render() {
        var chapter = chapterSelect.value;
        var ids = graph.nodes.map(function (n) { return n.id; });
        var context = [];
        if (chapter) {
          ids = ids.filter(function (id) { return graph.byId[id].chapter === chapter; });
          // Bring in direct prerequisites from other chapters, drawn dashed.
          ids.forEach(function (id) {
            graph.uses[id].forEach(function (u) {
              if (ids.indexOf(u) < 0 && context.indexOf(u) < 0) context.push(u);
            });
          });
        }
        view = { chapter: chapter, pages: ids.length, context: context.length };
        if (cy) cy.destroy();
        var all = ids.concat(context);
        cy = draw(canvas, graph, all, null, { layered: true, fixed: false });
        context.forEach(function (id) { cy.getElementById(id).addClass("context"); });
        cy.on("tap", "node", function (evt) { select(evt.target.id()); });
        cy.on("tap", function (evt) { if (evt.target === cy) clear(); });
        cy.on("dbltap", "node", function (evt) { window.location.href = evt.target.data("url"); });
        addTooltip(cy, canvas, graph);
        clear();
      }

      // With nothing selected, the status line says what is on screen.
      function clear() {
        cy.elements().removeClass("faded highlight focus shown");
        if (location.hash) history.replaceState(null, "", location.pathname + location.search);
        info.textContent = view.chapter
          ? "Showing the " + view.chapter + " chapter: " + count(view.pages, "page") +
            (view.context
              ? ", plus " + count(view.context, "prerequisite") +
                " from other chapters (dashed outline)."
              : ".")
          : "Showing all " + count(view.pages, "page") + ".";
      }

      function select(id) {
        var node = cy.getElementById(id);
        if (node.empty()) return;
        var ups = reach(graph.uses, id, Infinity);
        var downs = reach(graph.usedBy, id, Infinity);
        var lit = {};
        lit[id] = true;
        Object.keys(ups).concat(Object.keys(downs)).forEach(function (k) { lit[k] = true; });

        cy.batch(function () {
          cy.elements().removeClass("faded highlight focus shown");
          cy.nodes().forEach(function (n) { if (!lit[n.id()]) n.addClass("faded"); });
          cy.edges().forEach(function (e) {
            // Highlight edges on a path through the selected node only.
            var s = e.source().id(), t = e.target().id();
            var onUp = (s in ups || s === id) && (t in ups || t === id);
            var onDown = (s in downs || s === id) && (t in downs || t === id);
            if (onUp || onDown) e.addClass("highlight"); else e.addClass("faded");
          });
          node.addClass("focus");
          node.connectedEdges(".implied").removeClass("faded highlight").addClass("shown");
        });
        cy.animate({ center: { eles: node }, zoom: Math.max(cy.zoom(), 0.8) }, { duration: 250 });

        history.replaceState(null, "", "#" + id);
        var n = graph.byId[id];
        info.textContent = "";
        var link = document.createElement("a");
        link.href = n.url;
        link.textContent = n.title;
        var title = document.createElement(n.kind === "definition" ? "i" : "b");
        title.appendChild(link);
        info.appendChild(title);
        info.appendChild(document.createTextNode(
          " — " + (n.kind === "definition" ? "Definition" : "Theorem") + ", " + n.chapter + ". " +
          count(Object.keys(ups).length, "prerequisite") + "; " +
          count(Object.keys(downs).length, "page") + " build on it." +
          (node.connectedEdges(".implied").length
            ? " Dashed lines are direct links that a longer path already implies." : "") +
          " Click empty space to clear."));
      }

      function count(k, word) { return k + " " + word + (k === 1 ? "" : "s"); }

      function show(id) {
        if (!graph.byId[id]) return;
        if (cy.getElementById(id).empty()) { chapterSelect.value = ""; render(); }
        select(id);
      }

      // "input" fires when a suggestion is picked; "change" covers Enter.
      function onSearch() {
        var id = titleToId[search.value.trim().toLowerCase()];
        if (id) show(id);
      }
      search.addEventListener("input", onSearch);
      search.addEventListener("change", onSearch);
      chapterSelect.addEventListener("change", render);
      // "Try:" examples, e.g. data-graph-try="page:T/mean-value" or
      // "chapter:Differentiation".
      root.querySelectorAll("[data-graph-try]").forEach(function (button) {
        var spec = button.getAttribute("data-graph-try");
        var value = spec.slice(spec.indexOf(":") + 1);
        button.addEventListener("click", function () {
          search.value = "";
          if (spec.indexOf("page:") === 0) {
            show(value);
          } else {
            chapterSelect.value = value;
            render();
          }
        });
      });
      reset.addEventListener("click", function () {
        search.value = "";
        chapterSelect.value = "";
        render();
      });
      // graph#T/mean-value opens with that page selected. Read the hash
      // before the first render, which clears it.
      var initial = decodeURIComponent(location.hash.slice(1));
      render();
      if (initial) show(initial);
    }).catch(function (err) { showError(canvas, err); });
  }

  // ---------- boot ----------

  function boot() {
    document.querySelectorAll("[data-book-graph=page]").forEach(pageView);
    document.querySelectorAll("[data-book-graph=full]").forEach(fullView);
    document.querySelectorAll("[data-book-graph=feature]").forEach(featureView);
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", boot);
  else boot();
})();
