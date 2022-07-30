<template>
  <div class="q-pa-md">
    <q-table :grid="$q.screen.xs" :title="$t('heart.user')" :rows="rows" :columns="columns" row-key="id"
      :filter="filter">
      <template v-slot:top-right>
        <q-input borderless dense debounce="300" v-model="filter" placeholder="Search">
          <template v-slot:append>
            <q-icon name="search" />
          </template>
        </q-input>
      </template>
      <template v-slot:body="props">
        <q-tr clickable :props="props" @click="selectPatient(props.row)">
          <q-td key="name" :props="props">
            {{ props.row.name }} {{ props.row.last_name }}
          </q-td>

          <q-td key="email" :props="props">
            {{ props.row.email }}
          </q-td>
          <q-td key="created_at" :props="props">
            {{ props.row.created_at }}
          </q-td>
        </q-tr>
      </template>
    </q-table>
  </div>
</template>

<script>
import { ref } from "vue";
import api from "src/api";
export default {
  name: "patientsPage",
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
  methods: {
    getUsuarios() {
      api.get("users/").then((res) => { this.rows = res.data })
        .catch((error) => {
          console.error(error)
        })
    },

    selectPatient(obj) {
      sessionStorage.setItem("patient", JSON.stringify(obj))
      this.$emit("update:step", 2)
    },
  },
};
</script>
