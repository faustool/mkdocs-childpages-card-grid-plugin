# MkDocs Child Pages Card Grid Plugin

**Under development, use with caution!**

This plugin allows users to automatically add card grids on their pages with links to child pages.

Users can include card grids on all pages or configure using Markdown metadata to include or exclude specific pages.

TODO items:

- [ ] Add linters, build, versioning, tests, etc. Professional stuff 😄
- [ ] Add config to always include or exclude a page in their parent card grid.
- [ ] Add support to include `teaser` content from metadata, possibly in conjunction with the [wilhelmer/mkdocs-add-teaser plugin](https://github.com/wilhelmer/mkdocs-add-teaser).

## Config

```yaml
theme: 
  name: material
  features:
    - navigation.indexes

extra_css:
  - stylesheets/childpages_card_grid.css

plugins:
  - childpages-card-grid:
      # include card grids on all pages (default True)
      include_all: True
      # the title shown above the card grid (default: 'Child pages')
      cards_title: 'Child pages'
```

## Page Metadata

### `childpages_card_grid`

When `include_all: True`, it possible to exclude the card grid from a page with the metadata: `childpages_card_grid: exclude`.

Likewise, when `include_all: False`, it is possible to include the card grid in a page using `childpages_card_grid: include`.

### `childpages_card_grid_title`

It is possible to customize the card grid title of a specific page with the `childpages_card_grid_title` metadata.

## Sample childpages_card_grid.css

```css
.cards {
    max-width: 1200px;
    margin: 0 auto;
    display: grid;
    gap: 1rem;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
}

.card {
    /* Add shadows to create the "card" effect */
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
    transition: 0.3s;
}

.card_title {
    padding: 1rem 0 1rem 0;
    border-top: 1px;
    border-top-color: gray;
    border-top-style: solid;
}

.card:hover {
    /* On mouse-over, add a deeper shadow */
    box-shadow: 0 8px 16px 0 rgba(0, 0, 0, 0.2);
}

.card_container {
    /* Add some padding inside the card container */
    padding: 2px 16px;
}
```

## Limitations

This plugin was only tested with MkDocs Material Theme and the `navigation.indexes` feature enabled. It may be that other themes or other features of the Material theme generate a different `nav` tree and this plugin will not be able to figure out the parent/child pages.
