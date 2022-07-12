<template>
  <q-page padding>
    <q-toolbar inset>
      <q-breadcrumbs active-color="positive" style="font-size: 15px">
        <q-breadcrumbs-el icon="inventory_2" to="users" label="Usuarios" class="text-green" />
      </q-breadcrumbs>
    </q-toolbar>
    <div class="q-pa-md">
      <q-table :grid="$q.screen.xs" title="Usuarios" :rows="rows" :columns="columns" row-key="id" :filter="filter">
        <template v-slot:top-right>
          <q-btn flat color="green-6" icon-right="add" label="Crear" @click="go_tonew" />
          <q-input borderless dense debounce="300" v-model="filter" placeholder="Search">
            <template v-slot:append>
              <q-icon name="search" />
            </template>
          </q-input>
          <div class="col-auto">
            <q-btn color="grey-7" round flat icon="more_vert">
              <q-menu cover auto-close>
                <q-list>
                  <q-item clickable>
                    <q-item-section no-caps>Exportar</q-item-section>
                  </q-item>
                </q-list>
              </q-menu>
            </q-btn>
          </div>
        </template>
        <template v-slot:body="props">
          <q-tr clickable :props="props" @click="go_todetalle(props.row.id)">
            <q-td key="name" :props="props">
              {{ props.row.name }}
            </q-td>

            <q-td key="email" :props="props">
              {{ props.row.email }}
            </q-td>
            <q-td key="created_at" :props="props">
              {{ props.row.created_at }}
            </q-td>
            <q-td key="state" :props="props">
              {{ props.row.state }}
            </q-td>
          </q-tr>
        </template>
      </q-table>
    </div>
  </q-page>
</template>

<script>
import { ref } from "vue";

export default {
  name: "usuariosPage",
  data() {
    return {
      filter: ref(""),
      columns: [
        {
          name: "name",
          field: "name",
          required: true,
          label: "Nombre",
          align: "left",
          sortable: true,
        },
        {
          name: "email",
          align: "center",
          label: "Correo",
          field: "email",
          sortable: true,
        },

      ],
      rows: [],
    };
  },
  mounted() {
    this.getUsuarios();
  },
  computed: {

  },
  methods: {
    getUsuarios() {
      let token = sessionStorage.getItem("token")
      this.$api.get("users/", {
        headers: {
          Authorization: `Token ${token}`,
        }
      }).then((res) => { this.rows = res.data })
    },

    go_todetalle(id) {
      this.$router.push({
        name: 'user',
        params: { id: id },
      });
    },
    go_tonew(id) {
      this.$router.push({
        name: "user",
        params: { id: 0, action: "new" },
      });
    },
  },
};
</script>
