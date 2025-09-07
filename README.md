# Personal Website

My personal website showcasing my work as a ML Engineer, including projects, publications, and information about me.

## About This Repository

This repository contains a clean, modern personal website built with HTML, CSS, and minimal JavaScript. This website is designed to be deployed to GitHub Pages.

## Site Structure

- `index.html` - Homepage (About)
- `writing.html` - Links to writing across the web
- `about.html` - Redirects to `index.html`
- `blog.html` - Redirects to `writing.html`
- `css/` - Stylesheets for the website
- `img/` - Images used throughout the site
- `files/` - Static assets (e.g., JSON, PDFs)

### Writing list

The `writing.html` page renders a chronological list from `files/writing.json`.

Add entries in this format (newest entries first or unsorted — the page will sort by `date` descending):

```
[
  {
    "title": "Post title",
    "url": "https://medium.com/@danjsaund/...",
    "date": "2024-08-15" // ISO 8601 (YYYY-MM-DD)
  },
  {
    "title": "Another post",
    "url": "https://huggingface.co/blog/...",
    "date": "2024-05-02"
  }
]
```

Notes:
- `date` is optional but recommended for proper sorting.
- `title` falls back to the URL if omitted.
- You can mix links from Medium, Hugging Face, or anywhere.

## Local Development

For local development:
```bash
python -m http.server
```

Or if you have Node.js installed:
```bash
npx serve
```

## Deployment

The site is designed to be deployed to GitHub Pages. Simply push the files to your GitHub repository.

## License

MIT
