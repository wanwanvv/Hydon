import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      redirect: "/realtime",
      component: HelloWorld,
      children:[
        {
          path: "/realtime",
          name: "RealTime",
          redirect: "/realTime/mainPage",
          component: () =>
            import("../components/realTime"),
          children: [
            {
              path:"/realTime/mainPage",
              name:"mainPage",
              component: () =>
                import("../components/result/realTime/mainPage"),
               meta: {
                 firstMenu: '/realtime', // 主菜单 的 接口文档 高亮
                 secondMenu: '/realtime' // 接口文档的子菜单高亮
               }
            },
            {
              path:"/realTime/cpu",
              name:"cpu",
              component: () =>
                import("../components/result/realTime/cpu"),
               meta: {
                 firstMenu: '/realtime', // 主菜单 的 接口文档 高亮
                 secondMenu: '/realtime' // 接口文档的子菜单高亮
               }
            },
            {
              path: "/realTime/disk",
              name: "disk",
              component: () =>
                import("../components/result/realTime/disk"),
              meta: {
                firstMenu: '/realtime',
                secondMenu: '/realtime'
              }
            },
            {
              path: "/realTime/memory",
              name:"memory",
              component: () =>
                import("../components/result/realTime/memory"),
              meta: {
                firstMenu: '/realtime',
                secondMenu: '/realtime'
              }
            },
            {
              path: "/realTime/network",
              name:"network",
              component: () =>
                import("../components/result/realTime/network"),
              meta: {
                firstMenu: '/realtime',
                secondMenu: '/realtime'
              }
            }
          ]
        },
        {
          path: "/check",
          name: "Check",
          redirect: "/check/M1D1",
          component: () =>
            import("../components/Check"),
          children:[
            {
              path: "/check/M1D1",
              name: "M1D1",
              component: () =>
                import("../components/result/check/M1D1"),
              meta: {
                firstMenu: '/check', // 主菜单 的 接口文档 高亮
                secondMenu: '/check/M1D1' // 接口文档的子菜单高亮
              }
            },
            {
              path: "/check/M1D2",
              name: "M1D2",
              component: () =>
                import("../components/result/check/M1D2"),
              meta: {
                firstMenu: '/check', // 主菜单 的 接口文档 高亮
                secondMenu: '/check/M1D2' // 接口文档的子菜单高亮
              }
            },
            {
              path: "/check/M1D3",
              name: "M1D3",
              component: () =>
                import("../components/result/check/M1D3"),
              meta: {
                firstMenu: '/check', // 主菜单 的 接口文档 高亮
                secondMenu: '/check/M1D3' // 接口文档的子菜单高亮
              }
            }
          ]
        },
        {
          path: "/prediction",
          name: "Prediction",
          redirect: "/prediction/M1D0",
          component: () =>
            import("../components/Prediction"),
          children: [{
            path: "/prediction/M1D0",
            name: "M1D0",
            component: () =>
              import("../components/result/prediction/M1D0"),
            meta: {
              firstMenu: '/prediction', // 主菜单 的 接口文档 高亮
              secondMenu: '/prediction/M1D0' // 接口文档的子菜单高亮
            }
          },
            {
              path: "/prediction/M1D1",
              name: "M1D1",
              component: () =>
                import("../components/result/prediction/M1D1"),
              meta: {
                firstMenu: '/prediction', // 主菜单 的 接口文档 高亮
                secondMenu: '/prediction/M1D1' // 接口文档的子菜单高亮
              }
            },
          {
            path: "/prediction/M1D2",
            name: "M1D2",
            component: () =>
              import("../components/result/prediction/M1D2"),
            meta: {
              firstMenu: '/prediction', // 主菜单 的 接口文档 高亮
              secondMenu: '/prediction/M1D2' // 接口文档的子菜单高亮
            }
          },
            {
              path: "/prediction/M1D3",
              name: "M1D3",
              component: () =>
                import("../components/result/prediction/M1D3"),
              meta: {
                firstMenu: '/prediction', // 主菜单 的 接口文档 高亮
                secondMenu: '/prediction/M1D3' // 接口文档的子菜单高亮
              }
            }]
        }]
    }
  ]
})
