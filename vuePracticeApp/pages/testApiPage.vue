<template>
    <div id="target"></div>
</template>

<script>
export default {
  mounted() {
    const returnedData = this.getStarWarsData()
    const target = document.querySelector('#target')
    console.log('Returned Data', returnedData)
    // target.innerHTML = "<p>" + returnedData[0].name + "</p>"
  },

  data () {
    return {
      recievedData: [],
    };
  },

  methods: {
    async getStarWarsData() {
      const data = (await this.axios.get('https://swapi.dev/api/people/')
      .then((res) => {
          console.log(res.data)
          return res.data
      })
      )
      
    },
  },
};
</script>

<style></style>
