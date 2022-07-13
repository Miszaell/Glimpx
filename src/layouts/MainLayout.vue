<template>
  <q-layout view="lHh Lpr fff" class="bg-grey-1">
    <q-header elevated class="bg-white text-grey-8" height-hint="64">
      <q-toolbar class="GPL__toolbar" style="height: 64px">
        <q-toolbar-title v-if="$q.screen.gt.sm" shrink class="row items-center no-wrap">
          <span class="q-ml-sm cursor-pointer" @click="$router.push('/')">{{ $t("main.appTitle") }}</span>
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
          <q-btn round flat icon="login" to="auth">
            <q-tooltip>Login</q-tooltip>
          </q-btn>
          <!-- <q-btn round flat>
            <q-avatar size="26px">
              <img src="https://cdn.quasar.dev/img/boy-avatar.png" />
            </q-avatar>
            <q-tooltip>Account</q-tooltip>
          </q-btn> -->
        </div>
      </q-toolbar>
    </q-header>
    <q-page-container>
      <router-view />
    </q-page-container>
    <q-footer bordered class="bg-white text-black flex flex-center">
      <q-item clickable to="contacto">
        <q-item-section>Contacto</q-item-section>
      </q-item>
      <q-item clickable to="mapa">
        <q-item-section>Mapa</q-item-section>
      </q-item>
    </q-footer>
  </q-layout>
</template>

<script>
import { ref } from "vue";
const stringOptions = ["hlPromotions"];
export default {
  name: "MainLayout",

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
    };
  },

  methods: {
    setLanguage(locale) {
      this.$root.$i18n.locale = locale;
    },
    currentLanguage() {
      return this.$i18n.locale === "es-MX" ? "en-US" : this.$i18n.locale;
    },
  },
};
</script>

<style lang="sass">
.GPL

  &__toolbar
    height: 64px

  &__toolbar-input
    width: 35%

  &__drawer-item
    line-height: 24px
    border-radius: 0 24px 24px 0
    margin-right: 12px

    .q-item__section--avatar
      padding-left: 12px
      .q-icon
        color: #5f6368

    .q-item__label:not(.q-item__label--caption)
      color: #3c4043
      letter-spacing: .01785714em
      font-size: .875rem
      font-weight: 500
      line-height: 1.25rem

    &--storage
      border-radius: 0
      margin-right: 0
      padding-top: 24px
      padding-bottom: 24px

  &__side-btn
    &__label
      font-size: 12px
      line-height: 24px
      letter-spacing: .01785714em
      font-weight: 500

  @media (min-width: 1024px)
    &__page-container
      padding-left: 94px
</style>
