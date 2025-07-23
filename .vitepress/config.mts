import { defineConfig } from 'vitepress'

// https://vitepress.dev/reference/site-config
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
  }
})
