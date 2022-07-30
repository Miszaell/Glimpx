import { Notify } from "quasar";
const routes = [
  {
    path: "/admin",
    name: "admin",
    component: () => import("src/layouts/AdminLayout.vue"),
    children: [
      { path: "", component: () => import("pages/IndexPage.vue") },
      {
        path: "/perfil",
        name: "perfil",
        component: () => import("src/pages/perfil/Perfil.vue"),
      },
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
      {
        path: "/stock",
        name: "stock",
        props: true,
        component: () => import("src/pages/inventario/Inventario.vue"),
      },
      {
        path: "/stockDetail",
        name: "stockDetail",
        props: true,
        component: () => import("src/pages/inventario/InventarioDetail.vue"),
      },
      {
        path: "/promotions",
        name: "promotions",
        props: true,
        component: () => import("src/pages/promociones/Promociones.vue"),
      },
      {
        path: "/promotionDetail",
        name: "promotionDetail",
        props: true,
        component: () => import("src/pages/promociones/PromocionDetail.vue"),
      },
      {
        path: "/emergency",
        name: "emergency",
        props: true,
        component: () => import("src/pages/emergencias/Emergencias.vue"),
      },
      {
        path: "/anamnesis",
        name: "anamnesis",
        props: true,
        component: () =>
          import("src/pages/emergencias/anamnesis/Anamnesis.vue"),
      },

      {
        path: "/anamnesisDetail",
        name: "anamnesisDetail",
        props: true,
        component: () =>
          import("src/pages/emergencias/anamnesis/AnamnesisDetail.vue"),
        beforeEnter: (next) => {
          if (!sessionStorage.getItem("data")) {
            Notify.create({
              type: "negative",
              position: "top-right",
              message:
                "La ruta 'Detalle de anamnesis' necesita algunos datos para ser accesible",
            });
            return false;
          }
        },
      },
      {
        path: "/manageAnamnesis",
        name: "manageAnamnesis",
        props: true,
        component: () =>
          import("src/pages/emergencias/anamnesis/ManageAnamnesis.vue"),
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
      {
        path: "/mapa",
        name: "mapa",
        props: true,
        component: () => import("src/pages/mapa/Mapa.vue"),
      },
      {
        path: "/aviso",
        name: "aviso",
        props: true,
        component: () => import("src/pages/aviso/Aviso.vue"),
      },
    ],
  },
  {
    path: "/auth",
    name: "auth",
    component: () => import("src/pages/Auth.vue"),
    beforeEnter: (to, from, next) => {
      if (sessionStorage.getItem("token")) {
        next("/admin");
      } else {
        next();
      }
    },
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: "/:catchAll(.*)*",
    component: () => import("pages/ErrorNotFound.vue"),
  },
];

export default routes;
