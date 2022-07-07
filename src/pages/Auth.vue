<template>
  <q-layout view="lHh Lpr fff" class="bg-grey-1">
    <q-header elevated class="bg-white text-grey-8" height-hint="64">
      <q-toolbar class="GPL__toolbar" style="height: 64px">
        <q-toolbar-title v-if="$q.screen.gt.sm" shrink class="row items-center no-wrap cursor-pointer"
          @click="$router.push('/')">
          <span class="q-ml-sm">{{ $t("main.appTitle") }}</span>
        </q-toolbar-title>

        <q-space />

        <q-select ref="search" dense borderless color="white" use-input class="GL__toolbar-select text-black"
          label="Search or jump to..." v-model="text" :options="filteredOptions" @filter="filter" style="width: 400px">
          <template v-slot:no-option>
            <q-item class="bg-white">
              <q-item-section>
                <div class="text-center">
                  <q-spinner-pie color="grey-5" size="24px" />
                </div>
              </q-item-section>
            </q-item>
          </template>

          <template v-slot:option="scope">
            <q-item v-bind="scope.itemProps" class="GL__select-GL__menu-link bg-white">
              <q-item-section side>
                <q-icon name="collections_bookmark" color="black" />
              </q-item-section>
              <q-item-section>
                <q-item-label v-html="$t(`dashboard.menu.${scope.opt.label}`)" class="text-black" />
              </q-item-section>
              <q-item-section side :class="{ 'default-type': !scope.opt.type }">
                <q-btn outline dense no-caps text-color="blue-grey-5" size="12px" class="bg-grey-1 q-px-sm">
                  {{ scope.opt.type || "Jump to" }}
                  <q-icon name="subdirectory_arrow_left" size="14px" />
                </q-btn>
              </q-item-section>
            </q-item>
          </template>
        </q-select>
        <q-space />

        <div class="q-gutter-sm row items-center no-wrap">
          <q-btn round dense flat color="text-grey-7" icon="translate">
            <q-menu :offset="[50, 10]">
              <q-list style="min-width: 50px">
                <q-item clickable v-close-popup @click="setLanguage('es-MX')">
                  <q-item-section>ES MX</q-item-section>
                </q-item>
                <q-item clickable v-close-popup @click="setLanguage('en-US')">
                  <q-item-section>EN US</q-item-section>
                </q-item>
              </q-list>
            </q-menu>
          </q-btn>
        </div>
      </q-toolbar>
    </q-header>
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
                <sign-in />
              </q-tab-panel>

              <q-tab-panel name="sign_up">
                <sign-up />
              </q-tab-panel>
            </q-tab-panels>
          </div>
        </div>
      </div>
    </q-page-container>
  </q-layout>
</template>

<script>
import { ref } from 'vue'
import SignIn from 'src/components/SignIn.vue'
import SignUp from 'src/components/SignUp.vue'
const stringOptions = ["hlPromotions"];
export default {
  name: "AuthPage",
  components: {
    SignIn,
    SignUp
  },
  setup() {
    const storage = ref(0.26);
    const text = ref("");
    const options = ref(null);
    const filteredOptions = ref([]);
    const search = ref(null); // $refs.search

    function filter(val, update) {
      if (options.value === null) {
        // load data
        setTimeout(() => {
          options.value = stringOptions;
          search.value.filter("");
        }, 1000);
        update();
        return;
      }
      if (val === "") {
        update(() => {
          filteredOptions.value = options.value.map((op) => ({ label: op }));
        });
        return;
      }
      update(() => {
        filteredOptions.value = [
          {
            label: val,
            type: "In this repository",
          },
          {
            label: val,
            type: "All GitHub",
          },
          ...options.value
            .filter((op) => op.toLowerCase().includes(val.toLowerCase()))
            .map((op) => ({ label: op })),
        ];
      });
    }

    return {
      text,
      options,
      filteredOptions,
      search,
      filter,
      storage,
      tab: ref('sign_in')
    };
  },

  methods: {
    setLanguage(locale) {
      this.$root.$i18n.locale = locale;
    },
    currentLanguage() {
      return this.$i18n.locale === "es-MX" ? "en-US" : this.$i18n.locale;
    },
  }
}
</script>
