<template>
  <div class="q-pa-md q-gutter-sm">
    <q-page-container class="GPL__page-container">
      <div class="flex flex-center q-mt-xl">
        <div style="min-width: 600px">
          <q-tabs v-model="tab" align="justify" narrow-indicator class="q-mb-lg">
            <q-tab class="text-purple" name="sign_in" :label="$t('main.login')" />
            <q-tab class="text-orange" name="sign_up" :label="$t('main.signUp')" />
          </q-tabs>

          <div class="q-gutter-y-sm">
            <q-tab-panels v-model="tab" animated transition-prev="scale" transition-next="scale" class="text-center">
              <q-tab-panel name="sign_in">
                <form-contact-vue />

              </q-tab-panel>

              <q-tab-panel name="sign_up">
                <contact-info-vue />
              </q-tab-panel>
            </q-tab-panels>
          </div>
        </div>
      </div>
    </q-page-container>
  </div>
</template>

<script>
import { ref } from 'vue'
import FormContactVue from 'src/components/FormContact.vue'
import ContactInfoVue from 'src/components/ContactInfo.vue'

export default {
  name: "contactoPage",
  components: {
    FormContactVue,
    ContactInfoVue
  },
  setup() {
    return {
      tab: ref('sign_in')

    }
  }
}
</script>
