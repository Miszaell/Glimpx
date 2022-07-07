<template>
  <div class="q-pa-md q-gutter-sm">
    <q-tree :nodes="simple" node-key="label" no-connectors efault-expand-all v-model:expanded="expanded">
      <template v-slot:default-body="prop">
        <div v-if="prop.node.link">
          <q-item clickable :to="prop.node.link">
            <q-item-label class="text-black">
              {{ prop.node.sec }}
            </q-item-label>
          </q-item>
        </div>
      </template>
    </q-tree>
  </div>
</template>

<script>
import { ref } from 'vue'

export default {
  name: "contactoPage",
  setup() {
    return {
      expanded: ref(['Satisfied customers (with avatar)', 'Good food (with icon)']),

      simple: [
        {
          label: 'Homepage',
          avatar: 'https://cdn.quasar.dev/img/boy-avatar.png',
          children: [
            {
              label: 'Login',
              icon: 'login',
              children: [
                {
                  icon: "person",
                  label: 'Usuarios',
                  link: "users",
                  sec: "Editar usuario"
                },
                {
                  label: 'Good service (disabled node with icon)',
                  icon: 'room_service',
                  children: [
                    { label: 'Prompt attention' },
                  ]
                },
                {
                  label: 'Pleasant surroundings (with icon)',
                  icon: 'photo',
                  children: [
                    {
                      label: 'Happy atmosphere (with image)',
                    },
                  ]
                }
              ]
            },

          ]
        }
      ]
    }
  }
}
</script>
