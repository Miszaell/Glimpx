<template>
  <q-page padding>
    <q-toolbar inset>
      <q-breadcrumbs active-color="positive" style="font-size: 15px">
        <q-breadcrumbs-el icon="inventory_2" label="Inventario" class="text-green" />
      </q-breadcrumbs>
    </q-toolbar>
    <div class="q-pa-md">
      <q-table :grid="$q.screen.xs" title="Inventario" :rows="rows" :columns="columns" row-key="id" :filter="filter">
        <template v-slot:top-right>
          <q-btn flat color="green-6" icon-right="add" label="Crear" to="stockDetail" />
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
            <q-td key="name" :props="props">
              {{ props.row.name }}
            </q-td>

            <q-td key="description" :props="props">
              {{ props.row.description }}
            </q-td>
            <q-td key="quantity" :props="props">
              {{ props.row.quantity }}
            </q-td>
            <q-td key="uom" :props="props">
              {{ props.row.uom }}
            </q-td>
          </q-tr>
        </template>
      </q-table>
    </div>
  </q-page>
</template>

<script>
import { ref } from 'vue';
import { Notify } from 'quasar';
import api from 'src/api';
export default {
  name: "inventarioPage",
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
          name: "description",
          field: "description",
          align: "center",
          label: "Descripción",
          sortable: true,
        },
        {
          name: "quantity",
          field: "quantity",
          required: true,
          label: "Cantidad",
          align: "left",
          sortable: true,
        },
        {
          name: "uom",
          field: "uom",
          required: true,
          label: "UOM",
          align: "left",
          sortable: true,
        },

      ],
      rows: [],
    };
  },
  mounted() {
    this.getData();
  },
  methods: {
    getData() {
      api.get("materials/").then((res) => { this.rows = res.data.rows })
        .catch((error) => {
          console.error(error)
        })
    },

    async goToDetalle(id) {

      try {
        let res = await api.get(`materials/${id}/`)
        sessionStorage.setItem("data", JSON.stringify(res.data))
        if (sessionStorage.getItem("data")) {
          this.$router.push({
            name: 'stockDetail',
            params: { method: 'put' }
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
}
</script>
