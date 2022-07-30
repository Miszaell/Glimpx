<template>
  <q-page padding>
    <q-toolbar inset>
      <q-breadcrumbs active-color="positive" style="font-size: 15px">
        <q-breadcrumbs-el icon="inventory_2" label="Consultas" class="text-green" />
      </q-breadcrumbs>
    </q-toolbar>
    <div class="q-pa-md">
      <q-table :grid="$q.screen.xs" title="Consultas" :rows="rows" :columns="columns" row-key="id" :filter="filter">
        <template v-slot:top-right>
          <q-btn flat color="green-6" icon-right="add" label="Crear" to="ManageAnamnesis" />
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
          <q-tr clickable :props="props" @click="goToDetalle(props.row.id)">
            <q-td key="username" :props="props">
              {{ props.row.username }}
            </q-td>

            <q-td key="modified_date" :props="props">
              {{ props.row.modified_date }}
            </q-td>
          </q-tr>
        </template>
      </q-table>
    </div>
  </q-page>
</template>

<script>
import { ref } from "vue";
import { Notify } from "quasar";
import api from "src/api";
export default {
  name: "emergenciasPage",
  data() {
    return {
      filter: ref(""),
      columns: [
        {
          name: "username",
          field: "username",
          required: true,
          label: "Nombre",
          align: "left",
          sortable: true,
        },
        {
          name: "modified_date",
          align: "center",
          label: "Ultima modificación",
          field: "modified_date",
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
      api.get("anamnesis/").then((res) => { this.rows = res.data })
        .catch((error) => {
          console.error(error)
        })
    },

    async goToDetalle(id) {

      try {
        let res = await api.get(`anamnesis/${id}/`)
        sessionStorage.setItem("data", JSON.stringify(res.data))
        if (sessionStorage.getItem("data")) {
          this.$router.push({
            name: 'anamnesis',
          });
        } else {
          Notify.create({
            type: "negative",
            position: "top-right",
            message: "Ocurrió un error inesperado, intenta otra vez.",
          });
        }
      } catch (error) {
        console.error(error)
        Notify.create({
          type: "negative",
          position: "top-right",
          message: "Ocurrió un error inesperado, intenta otra vez.",
        });
      }
    },
  },
};
</script>
