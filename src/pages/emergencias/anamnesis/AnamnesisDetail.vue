<template>
  <q-page padding>
    <div>
      <q-toolbar inset>
        <q-breadcrumbs active-color="positive" style="font-size: 15px">
          <q-breadcrumbs-el icon="inventory_2" to="anamnesis" label="Anamnesis" />
          <q-breadcrumbs-el v-if="!row.username" icon="add" label="Crear" class="text-green" />
          <q-breadcrumbs-el :label="`Detalle de anamnesis: ${row.username}`" class="text-green" />
        </q-breadcrumbs>
      </q-toolbar>
      <q-card flat bordered class="my-card bg-grey-1 text-black q-mb-md">
        <q-card-section>
          <div class="row items-center no-wrap">
            <div class="col">
              <div class="text-h6">{{ row.username }}</div>
            </div>
          </div>
        </q-card-section>
        <q-card-section>
          <q-form class="q-gutter-md">
            <q-card-section horizontal>
              <q-card-section class="col-6">
                <q-input readonly class="q-ma-sm" filled v-model="user.name" label="Nombre" dense />
                <q-input readonly class="q-ma-sm" filled v-model="user.email" label="Correo" dense />
                <q-input readonly class="q-ma-sm" filled v-model="user.phone" label="Telefono" dense />
                <q-input readonly class="q-ma-sm" filled v-model="user.address" label="Dirección" dense />
              </q-card-section>
              <q-separator vertical />
              <q-card-section class="col-6">
                <q-input readonly class="q-ma-sm" filled v-model="user.curp" label="CURP" dense />
                <q-input readonly class="q-ma-sm" filled v-model="user.university_id" label="Matricula" dense />
                <q-input readonly class="q-ma-sm" filled v-model="user.ssn" label="NSS" dense />
                <q-input readonly class="q-ma-sm" filled v-model="user.date_of_birth" label="Fecha de nacimiento"
                  dense />
                <q-input readonly class="q-ma-sm" filled v-model="user.gender" label="Genero" dense />
              </q-card-section>
            </q-card-section>
          </q-form>
        </q-card-section>
      </q-card>
    </div>
    <PhysicDetail />
    <ClinicDetail />
    <FamilyDetail />
  </q-page>
</template>

<script>
import { ref } from "vue";
import PhysicDetail from "pages/emergencias/physic/Physic.vue"
import FamilyDetail from "../family/Family.vue";
import ClinicDetail from "../clinic/Clinic.vue";
export default {
  name: "emergenciasPage",
  components: {
    PhysicDetail,
    FamilyDetail,
    ClinicDetail
  },
  data() {
    return {
      row: ref([]),
      user: ref([]),
    };
  },
  created() {
    if (sessionStorage.getItem("data")) {
      this.getData();
    }
  },
  unmounted() {
    sessionStorage.removeItem("data")
  },
  methods: {
    getData() {
      let res = JSON.parse(sessionStorage.getItem("data"))
      this.user = res.user;
      this.row = res;
    },

  },
};
</script>
