<template>
  <div>
    <div id="container"></div>
  </div>
</template>

<script>
import Highcharts from "../assets/highChartsGantt.js";

export default {
  mounted() {
    this.initGantt();
  },

  data: () => {
    return {};
  },

  methods: {
    // initializes the gantt chart
    initGantt() {
      Highcharts.ganttChart("container", {
        title: {
          text: "Gantt Chart with Navigation",
        },

        yAxis: {
          uniqueNames: true,
        },

        navigator: {
          enabled: true,
          liveRedraw: true,
          series: {
            type: "gantt",
            pointPlacement: 0.5,
            pointPadding: 0.25,
          },
          yAxis: {
            min: 0,
            max: 3,
            reversed: true,
            categories: [],
          },
        },

        rangeSelector: {
          enabled: true,
          buttons: [
            {
              type: "day",
              count: 7,
              text: "7d",
              title: "View 7 Day",
            },
            {
              type: "month",
              count: 1,
              text: "m",
              title: "View 1 Month",
            },
            {
              type: "year",
              count: 1,
              text: "y",
              title: "View 1 Year",
            },
            {
              type: "all",
              text: "all",
              title: "View all",
            },
          ],
        },

        scrollbar: {
          enabled: true,
        },

        series: [
          {
            // the name of the overall fleet
            name: "Fleet 1 ",
            // the data that will be pulled from an api
            data: [
              // CLASS 1 --------------------------------------------
              {
                start: Date.UTC(2017, 11, 1),
                end: Date.UTC(2017, 11, 1),
                name: "Class 1",
                id: "class1",
              },
              // CLASS 1 PLATFORM 1 --------------------------------------------
              {
                start: Date.UTC(2017, 11, 1),
                end: Date.UTC(2018, 1, 2),
                name: "Platform 1",
                id: "platform1_1",
                parent: "class1",
                inport: true,
                color: '#001021'
              },
              {
                start: Date.UTC(2017, 11, 1),
                end: Date.UTC(2018, 1, 2),
                name: "Platform 1 Details",
                id: "platform1_1_details",
                parent: "class1",
                inport: true,
                color: '#001021'
              },
              {
                start: Date.UTC(2018, 1, 2),
                end: Date.UTC(2018, 3, 7),
                name: "Platform 1",
                id: "platform1_1",
                parent: "class1",
                inport: false,
                color: '#1481BA'
              },
              {
                start: Date.UTC(2017, 11, 1),
                end: Date.UTC(2018, 1, 2),
                name: "Platform 1 Details",
                id: "platform1_1_details",
                parent: "class1",
                inport: true,
                color: '#001021'
              },
              // CLASS 1 PLATFORM 2 --------------------------------------------
              {
                start: Date.UTC(2017, 12, 12),
                end: Date.UTC(2018, 1, 14),
                name: "Platform 2",
                id: "platform2_1",
                parent: "class1",
                inport: false,
                color: '#1481BA'
              },
              {
                start: Date.UTC(2017, 11, 1),
                end: Date.UTC(2018, 1, 2),
                name: "Platform 2 Details",
                id: "platform1_2_details",
                parent: "class1",
                inport: true,
                color: '#001021'
              },
              {
                start: Date.UTC(2018, 1, 14),
                end: Date.UTC(2018, 2, 25),
                name: "Platform 2",
                id: "platform2_1",
                parent: "class1",
                inport: true,
                color: '#001021'
              },
              {
                start: Date.UTC(2017, 11, 1),
                end: Date.UTC(2018, 1, 2),
                name: "Platform 2 Details",
                id: "platform1_2_details",
                parent: "class1",
                inport: true,
                color: '#001021'
              },
              // CLASS 2 --------------------------------------------
              {
                start: Date.UTC(2017, 11, 1),
                end: Date.UTC(2017, 11, 1),
                name: "Class 2",
                id: "class2",
              },
              // CLASS 2 PLATFORM 1 --------------------------------------------
              {
                start: Date.UTC(2017, 11, 10),
                end: Date.UTC(2017, 12, 5),
                name: "Platform 1",
                id: "platform1_2",
                parent: "class2",
                inport: true,
                color: '#001021'
              },
              {
                start: Date.UTC(2017, 11, 1),
                end: Date.UTC(2018, 1, 2),
                name: "Platform 1 Details",
                id: "platform1_1_details",
                parent: "class2",
                inport: true,
                color: '#001021'
              },
              {
                start: Date.UTC(2017, 12, 6),
                end: Date.UTC(2017, 12, 29),
                name: "Platform 1",
                id: "platform1_2",
                parent: "class2",
                inport: false,
                color: '#1481BA'
              },
            ],
          },
        ],
      });
    },
  },
};
</script>

<style>
#container {
  max-width: 800px;
  margin: 1em auto;
}
</style>
