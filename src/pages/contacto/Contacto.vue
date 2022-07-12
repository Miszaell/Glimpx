<template>
  <div class="q-pa-md q-gutter-sm">
    <q-page-container class="GPL__page-container">
      <div class="flex flex-center q-mt-xl">
        <div style="min-width: 600px">
          <q-tabs v-model="tab" align="justify" narrow-indicator class="q-mb-lg">
            <q-tab class="text-purple" name="contactus" :label="$t('main.contactForm')" />
            <q-tab class="text-orange" name="contactinf" :label="$t('main.contactInfo')" />
          </q-tabs>

          <div class="q-gutter-y-sm">
            <q-tab-panels v-model="tab" animated transition-prev="scale" transition-next="scale" class="text-center">
              <q-tab-panel name="contactus">
                <form-contact-vue />

              </q-tab-panel>

              <q-tab-panel name="contactinf">
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
      tab: ref('contactus')

    }
  }
}
</script>
