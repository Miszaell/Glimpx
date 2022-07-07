const routes = [
  {
    path: "/admin",
    name: "admin",
    component: () => import("src/layouts/AdminLayout.vue"),
    children: [
      { path: "", component: () => import("pages/IndexPage.vue") },
      {
        path: "/users",
        name: "users",
        component: () => import("src/pages/users/Users.vue"),
      },
      {
        path: "/user-detail",
        name: "user",
        props: true,
        component: () => import("src/pages/users/UserDetail.vue"),
      },
    ],
    meta: {
      requiresAuth: true,
    },
  },
  {
    path: "/",
    name: "public",
    component: () => import("layouts/MainLayout.vue"),
    children: [
      { path: "", component: () => import("pages/IndexPage.vue") },
      {
        path: "/contacto",
        name: "contacto",
        props: true,
        component: () => import("src/pages/contacto/Contacto.vue"),
      },
    ],
  },
  {
    path: "/auth",
    name: "auth",
    component: () => import("src/pages/Auth.vue"),
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: "/:catchAll(.*)*",
    component: () => import("pages/ErrorNotFound.vue"),
  },
];

export default routes;
