# Changelog - SuggestoAI Site

All notable changes to the suggestoai-site project will be documented in this file.

## [2025-01-21] - Blog System Implementation

### Added
- **Blog System**: Complete blog infrastructure with `/blog/` folder structure
  - `blog/index.html` - Main blog page with dynamic post loading
  - `blog/posts/` - Directory for individual blog posts
  - `blog/posts/template.html` - HTML template for blog posts
  - `blog/posts/posts.json` - Metadata storage for all posts
  - `blog/rss.xml` - RSS 2.0 feed for blog subscription
  - `blog/README.md` - Comprehensive documentation

### Enhanced
- **publish_post.py**: Extended with new capabilities
  - JSON input support for external agent integration
  - HTML blog post generation from template
  - Automatic Git commit and push functionality
  - SEO meta tags integration
  - RSS feed updates
  - Sitemap updates
  - Related posts functionality

### Modified
- **Navigation**: Added "Blog" link to all main site pages
  - `index.html`
  - `ai-recommends.html`
  - `for-brands.html`
  - `about.html`
  - `terms.html`
  - `delete-data.html`

- **Sitemap**: Enhanced `sitemap.xml` with blog URLs and detailed metadata
- **Dependencies**: Updated `requirements.txt` with `beautifulsoup4` and `lxml`

### Technical Details
- **SEO Optimization**: Open Graph, Twitter Cards, structured data
- **Responsive Design**: Mobile-friendly blog layout
- **Social Sharing**: Built-in sharing buttons for Twitter, Facebook, LinkedIn
- **Related Posts**: Dynamic loading of related content
- **RSS Feed**: Standard RSS 2.0 format for content syndication

### Files Created
- `blog/index.html` (Main blog listing page)
- `blog/posts/template.html` (Blog post template)
- `blog/posts/posts.json` (Post metadata storage)
- `blog/rss.xml` (RSS feed)
- `blog/README.md` (Documentation)

### Files Modified
- `publish_post.py` (Extended functionality)
- `index.html` (Added blog navigation)
- `ai-recommends.html` (Added blog navigation)
- `for-brands.html` (Added blog navigation)
- `about.html` (Added blog navigation)
- `terms.html` (Added blog navigation)
- `delete-data.html` (Added blog navigation)
- `sitemap.xml` (Added blog URLs)
- `requirements.txt` (Added dependencies)

### Testing
- Created and tested demo blog post: "Best Wireless Earbuds 2025: AI-Powered Recommendations"
- Verified JSON input functionality
- Confirmed Git automation works correctly
- Tested RSS feed generation
- Validated sitemap updates

---

## [Previous Changes]
*Document previous changes here as needed*

---

## How to Use This Changelog

### Format
- **Added**: New features
- **Enhanced**: Improved existing features
- **Modified**: Changes to existing functionality
- **Fixed**: Bug fixes
- **Removed**: Deprecated features

### Version Format
- Use semantic versioning: `[YYYY-MM-DD] - Description`
- Include detailed technical information
- List all affected files
- Document testing procedures

### Maintenance
- Update this file after each significant change
- Include both technical and user-facing changes
- Document any breaking changes clearly
- Keep entries concise but informative 