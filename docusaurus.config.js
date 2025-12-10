
const settings = require('./.docsaurus/setting.js');

module.exports = {
  title: settings.title,
  tagline: settings.tagline,
  url: settings.url,
  baseUrl: settings.baseUrl,
  onBrokenLinks: settings.onBrokenLinks,
  onBrokenMarkdownLinks: settings.onBrokenMarkdownLinks,
  favicon: settings.favicon,
  organizationName: settings.organizationName, // Usually your GitHub org/user name.
  projectName: settings.projectName, // Usually your repo name.
  themeConfig: settings.themeConfig,
  presets: settings.presets,
};
