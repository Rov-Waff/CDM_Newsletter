import { defineConfig } from 'vitepress'
import { RSSOptions, RssPlugin } from 'vitepress-plugin-rss';

// https://vitepress.dev/reference/site-config
const base_url="https://cdm-newsletter.pages.dev"
const rssOptions: RSSOptions = {
  title: '站点名称',
  baseUrl: base_url,
  copyright: '版权声明',
  // 可选：作者、描述等
};
export default defineConfig({
  title: "猫站小报",
  description: "做最优质的社区报刊",
  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    nav: [
      { text: '主页', link: '/' },
      { text: '投稿', link: '/upload' }
    ],

    sidebar: [
      {
        text: '读者须知',
        items: [
          { text: '阅读指南', link: '/read' },
          { text: '投稿指南', link: '/upload' },
          { text:"帖子传送门",link:"/portal"},
          { text:"贡献指南",link:"/contribute" }
        ]
      }
    ],

    socialLinks: [
      { icon: 'github', link: 'https://github.com/Rov-Waff/CDM_Newsletter' }
    ]
  },vite:{
    plugins:[RssPlugin(rssOptions)]
  }
})
