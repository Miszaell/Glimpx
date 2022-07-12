<template>
  <div class="q-pa-md q-gutter-sm">
    <q-tree :nodes="simple" node-key="label" no-connectors efault-expand-all v-model:expanded="expanded">

    </q-tree>
  </div>
</template>

<script>
import { ref } from 'vue'

export default {
  name: "MapaPage",
  setup() {
    return {
      expanded: ref(['Satisfied customers (with avatar)', 'Good food (with icon)']),

      simple: [
        {
          label: 'Homepage',
          icon: 'home',
          children: [
            {
              label: 'Login',
              icon: 'login',
              children: [
                {
                  icon: "person",
                  label: 'Usuarios',
                  link: "users",
                  children: [
                    {
                      label: "Gestionar usuario",
                      icon: 'person_search'
                    }
                  ],
                },
                {
                  label: 'Inventario',
                  icon: 'inventory',
                  children: [
                    {
                      label: 'Gestionar inventario',
                      icon: 'inventory'
                    },
                  ]
                },
                {
                  label: 'Promociones de Salud',
                  icon: 'health_and_safety',
                  children: [
                    {
                      label: 'Gestionar promociones',
                      icon: 'rate_review'
                    },

                  ]
                },
                {
                  label: 'Emergencias',
                  icon: 'emergency',
                  children: [
                    {
                      label: 'Gestionar emergencias',
                      icon: 'personal_injury'
                    },
                  ]

                },
                {
                  label: 'Configuración',
                  icon: 'settings',
                  children: [
                    {
                      label: 'Gestionar noticias',
                      icon: 'notifications_active'
                    },
                    {
                      label: 'Gestionar contenido',
                      icon: 'web'
                    },
                  ]
                },
                {
                  label: 'Roles',
                  icon: 'security',
                  children: [
                    {
                      label: 'Gestionar roles',
                      icon: 'admin_panel_settings'
                    },
                  ]

                },
              ]
            },
            {
              label: 'Contacto',
              icon: 'contact_mail',
            },
          ]
        }
      ]
    }
  }
}
</script>
