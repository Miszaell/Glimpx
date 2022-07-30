<template>
  <q-page padding>
    <q-toolbar inset>
      <q-breadcrumbs active-color="positive" style="font-size: 15px">
        <q-breadcrumbs-el icon="health_and_safety" label="Promociones de salud" class="text-green" />
      </q-breadcrumbs>
    </q-toolbar>
    <div class="q-pa-md">
      <q-table :grid="$q.screen.xs" title="Promociones de salud" :rows="rows" :columns="columns" row-key="id"
        :filter="filter">
        <template v-slot:top-right>
          <q-btn flat color="green-6" icon-right="add" label="Crear" to="promotionDetail" />
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
            <q-td key="title" :props="props">
              {{ props.row.title }}
            </q-td>

            <q-td key="description" :props="props">
              {{ props.row.description }}
            </q-td>
            <q-td key="startTime" :props="props">
              {{ props.row.startTime }}
            </q-td>
            <q-td key="endTime" :props="props">
              {{ props.row.endTime }}
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
  name: "promocionesPage",
  data() {
    return {
      filter: ref(""),
      columns: [
        {
          name: "title",
          field: "title",
          required: true,
          label: "Titulo",
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
          name: "startTime",
          field: "startTime",
          required: true,
          label: "Fecha de inicio",
          align: "left",
          sortable: true,
        },
        {
          name: "endTime",
          field: "endTime",
          required: true,
          label: "Fecha de termino",
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
      api.get("promotions/").then((res) => { this.rows = res.data.rows })
        .catch((error) => {
          console.error(error)
        })
    },

    async goToDetalle(id) {

      try {
        let res = await api.get(`promotions/${id}/`)
        sessionStorage.setItem("data", JSON.stringify(res.data))
        if (sessionStorage.getItem("data")) {
          this.$router.push({
            name: 'promotionDetail'
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
