# html-resource-embedder
embed all media/js/css into a static self-contained html

<!-- jooray-links:start -->
### More from me

**Related projects**

- [nowhere-webxdc](https://github.com/jooray/nowhere-webxdc): the nowhere offline URL renderer as a WebXDC app for Delta Chat
- [d21poll](https://github.com/jooray/d21poll): plus and minus voting for chat groups, as a WebXDC app

**Full project showcase:** [all my projects](https://juraj.bednar.io/showcase/).

I write about building things on [my blog](https://juraj.bednar.io/en/blog-en/). I also wrote a cypherpunk novel, [Tamers of Entropy](https://tamersofentropy.net/), and there is a [trailer](https://tamersofentropy.net/#trailer).
<!-- jooray-links:end -->

# Install

```
poetry install
```

# Usage


```
poetry run python html-resource-embedder.py input.html self-contained.html [--base-url BASE_URL] [--no-module-js]
```

Arguments:
- `input.html`: The input HTML file
- `self-contained.html`: The output HTML file
- `--base-url BASE_URL`: (Optional) Base URL or directory for resources (default: `./`)
- `--no-module-js`: (Optional) Do not wrap inlined JS as module scripts (default: wrap if export/import is detected)

By default, JS files containing `export` or `import` at the top level are wrapped in `<script type="module">`.

Example:
```
poetry run python html-resource-embedder.py index.html self-contained.html --base-url ./assets/
```
To disable module script wrapping:
```
poetry run python html-resource-embedder.py index.html self-contained.html --no-module-js
```
