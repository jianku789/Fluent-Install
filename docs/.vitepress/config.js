import { defineConfig } from 'vitepress'

export default defineConfig({
  title: 'FluentInstall',
  description: 'Fluent Design 版本的 Steam 游戏解锁工具',

  base: '/Fluent-Install/',

  head: [
    ['link', { rel: 'icon', href: '/icon.ico' }]
  ],

  themeConfig: {
    logo: '/icon.ico',
    nav: [
      { text: '首页', link: '/' },
      { text: '入门指南', link: '/guide/getting-started' },
      { text: '常见问题', link: '/faq/' },
      {
        text: '社区与交流',
        items: [
          { text: 'GitHub Issue', link: 'https://github.com/zhouchentao666/Fluent-Install/issues' },
          { text: 'Q群', link: 'https://qm.qq.com/q/gtTLap5Jw4' },
          { text: 'TG群', link: 'https://t.me/+vTrqXKpRJE9kNmVl' }
        ]
      }
    ],

    sidebar: [
      {
        text: '指南',
        items: [
          { text: '入门指南', link: '/guide/getting-started' }
        ]
      },
      {
        text: '常见问题',
        items: [
          { text: 'FAQ', link: '/faq/' }
        ]
      }
    ],

    footer: {
      message: 'FluentInstall',
      copyright: 'Copyright © 2024-present'
    },

    socialLinks: [
      { icon: 'github', link: 'https://github.com/zhouchentao666/Fluent-Install' }
    ]
  }
})
