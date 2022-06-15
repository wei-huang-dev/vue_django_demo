
<template>
  <v-app style="background: #ededed">
    <NavDrawer ref="drawer"></NavDrawer>
    <NavBar
      @toggle-drawer="$refs.drawer.drawer = !$refs.drawer.drawer"
    ></NavBar>

    <v-container>
      <v-row>
        <v-col cols="12">
          <v-card hover class="my-3">
            <v-card-title class="font-weight-black indigo--text darken-3">
              <v-icon large color="indigo darken--1" class="mr-2"
                >mdi-eye</v-icon
              >Visualização
            </v-card-title>
            <v-flex class="d-flex">
              <v-switch
                class="mx-4"
                v-model="switchTipo"
                label="Mostrar Gráfico de Tipo"
              ></v-switch>
              <v-switch
                class="mx-4"
                v-model="switchGrupo"
                label="Mostrar Gráfico de Grupos"
              ></v-switch>
              <v-switch
                class="mx-4"
                v-model="switchTable"
                label="Mostrar Tabela"
              ></v-switch>
            </v-flex>
          </v-card>
          <v-flex class="d-flex">
            <GraficoTipo
              class="mr-2"
              v-show="switchTipo == true"
              :dados="dados"
            />
            <GraficoGrupo v-show="switchGrupo == true" :dados="dados" />
          </v-flex>
          <Tabela v-show="switchTable == true" :dados="dados" />
        </v-col>
      </v-row>
      <v-btn
        v-scroll="onScroll"
        v-show="fab"
        fab
        dark
        fixed
        bottom
        right
        color="primary"
        @click="toTop"
      >
        <v-icon>mdi-arrow-up</v-icon>
      </v-btn>
    </v-container>
  </v-app>
</template>
    

<script>
import NavBar from "./NavBar";
import NavDrawer from "./NavDrawer";
import GraficoTipo from "./GraficoTipo";
import GraficoGrupo from "./GraficoGrupo";
import Tabela from "./Tabela";
import { Fragment } from "vue-fragment";
import { axios } from "@/plugins/axios";
export default {
  components: {
    NavBar,
    NavDrawer,
    GraficoTipo,
    GraficoGrupo,
    Tabela,
    Fragment,
  },
  data: () => ({
    dados: [],
    switchTipo: true,
    switchGrupo: true,
    switchTable: true,
    fab: false,
  }),
  methods: {
    onScroll(e) {
      if (typeof window === "undefined") return;
      const top = window.pageYOffset || e.target.scrollTop || 0;
      this.fab = top > 20;
    },
    toTop() {
      this.$vuetify.goTo(0);
    },
  },
  async mounted() {
    try {
      let response = await axios.get("https://api-psi-geadv.herokuapp.com/");
      this.dados = response.data
        .filter((e) => !isNaN(parseFloat(e.D3C) && isFinite(e.D3C)))
        .map((item, index, array) => {
          return {
            tipo: item.D2N,
            am_ref: parseFloat(item.D3C),
            grupo: item.D4N.replace(/\d*[.]?\d*/g, ""),
            variacao: parseFloat(item.V),
            ref: item.D3N.charAt(0).toUpperCase() + item.D3N.slice(1),
            key: index,
          };
        });
    } catch (err) {
      console.log(err);
    }
  },
};
</script>