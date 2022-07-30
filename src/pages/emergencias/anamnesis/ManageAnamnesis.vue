<template>
  <q-page class="bg-white q-pa-lg">
    <q-stepper v-model="step" ref="stepper" color="primary" active-color="positive" flat animated>
      <q-step :name="1" :title="$t('heart.user')" icon="person" :done="step > 1">
        <PatientDetail v-on:update:step="$refs.stepper.goTo($event)" />
      </q-step>

      <q-step :name="2" :title="$t('heart.physic')" icon="settings" :done="step > 2">
        <PhysicDetail :postReq="sendPost" v-on:update:step="$refs.stepper.goTo($event)" />
      </q-step>

      <q-step :name="3" :title="$t('heart.clinic')" icon="create_new_folder" :done="step > 3">
        <ClinicDetail v-on:update:step="$refs.stepper.goTo($event)" />
      </q-step>

      <q-step :name="4" :title="$t('heart.family')" icon="assignment">
        <FamilyDetail />
      </q-step>

      <template v-slot:navigation>
        <q-stepper-navigation>
          <q-btn @click="validateStepper()" flat color="primary" v-show="step !== 1"
            :label="step === 4 ? 'Finish' : 'Continue'" />

          <q-btn @click="$refs.stepper.goTo(3)" flat color="primary" label="Continue" />
          <q-btn v-if="step > 1" flat color="black" @click="$refs.stepper.previous()" label="Back" class="q-ml-sm" />
        </q-stepper-navigation>
      </template>
    </q-stepper>
  </q-page>
</template>
<script>
import { ref } from 'vue'
import FamilyDetail from '../family/Family.vue'
import ClinicDetail from '../clinic/Clinic.vue';
import PhysicDetail from '../physic/Physic.vue';
import PatientDetail from '../patient/Patient.vue';
export default {
  name: "ManageAnamnesis",
  components: {
    FamilyDetail,
    ClinicDetail,
    PhysicDetail,
    PatientDetail
  },
  setup() {
    return {
      step: ref(1),
    }
  },
  data() {
    return {
      sendPost: false,
    }
  },
  methods: {
    validateStepper() {
      this.sendPost = !this.sendPost
      this.$refs.stepper.next()
      // console.log(this.$refs.stepper.modelValue)

    }
  },
}
</script>
