import { defineConfig } from 'vitepress'
import mathjax3 from 'markdown-it-mathjax3'

import { RSSOptions, RssPlugin } from 'vitepress-plugin-rss';

const customElements = [  
'math', 'maction', 'maligngroup', 'malignmark', 'menclose', 'merror', 'mfenced', 'mfrac', 'mi', 'mlongdiv', 'mmultiscripts', 'mn', 'mo', 'mover', 'mpadded', 'mphantom', 'mroot', 'mrow', 'ms', 'mscarries', 'mscarry', 'msgroup', 'mstack', 'mlongdiv', 'msline', 'mspace', 'msqrt', 'msrow', 'mstyle', 'msub', 'msup', 'msubsup', 'mtable', 'mtd', 'mtext', 'mtr', 'munder', 'munderover'];
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
  markdown:{
    config:(md)=>{
      md.use(mathjax3)
    }
  },
  vue:{
    template:{
      compilerOptions:{
        isCustomElement:(tag)=>{
          customElements.includes(tag)
        }
      }
    }
  },
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
      },
      {
        text:"第三期",
        items:[
          {text:"编辑部专版",link:"/03/head"},
          {text:"积木纪元",link:"/03/kitten"},
          {text:"代码诗人",link:"/03/code"},
          {text:"传火者",link:"/03/tutorial"},
          {text:"撤硕儿",link:"/03/holy-posts"},
          {text:"后记",link:"/03/end"},
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
