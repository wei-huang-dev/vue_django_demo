<template>
  <v-app>
    <v-list>
      <v-list-item v-for="(item, i) in recievedData.results" :key="i">
        <v-list-item-content>
          <v-list-item-title v-text="item.name"></v-list-item-title>
          <p>Height: {{ item.height }}</p>
        </v-list-item-content>
      </v-list-item>
    </v-list>
    <!-- {{ recievedData }} -->
  </v-app>
</template>

<script>
export default {
  mounted() {
    this.getStarWarsData();
  },

  data() {
    return {
      recievedData: [],
    };
  },

  methods: {
    async getStarWarsData() {
      const response = await this.$axios.get("https://swapi.dev/api/people/");
      const results = response.data;
      this.recievedData = results;
      const parsedObject = JSON.parse(JSON.stringify(this.recievedData));
      console.log(parsedObject);
    },
  },

  computed: {
    
  },
};
</script>

<style></style>
