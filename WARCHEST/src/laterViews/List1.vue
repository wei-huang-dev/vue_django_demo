<template>
  <div class="about">
    <h1>Searchable List</h1>

    <v-card>
      <v-card-title>Search
        <v-spacer></v-spacer>
        <v-text-field v-model="search" append-icon="search" label="Search" single-line hide-details></v-text-field>
      </v-card-title>
    </v-card>

    <v-data-table
      :headers="headers"
      :items="data"
      item-key="id"
      class="elevation-1"
      :loading="loading"
      :search="search"
      v-model="selected"
      select-all
      hide-actions
      :pagination.sync="pagination"
    >
      <template v-slot:no-data>
        <v-alert :value="true" color="error" icon="warning">Sorry, nothing to display here :(</v-alert>
      </template>

      <template slot="headerCell" slot-scope="props">
        <v-tooltip bottom>
          <template v-slot:activator="{ on }">
            <span v-on="on">{{ props.header.text }}</span>
          </template>
          <span>{{ props.header.text }}</span>
        </v-tooltip>
      </template>

      <template v-slot:items="props">
        <!-- <tr @click="props.expanded = !props.expanded"> -->
        <td>
          <v-checkbox
            :name="'checkbox'+props.item.id"
            :value="props.item"
            v-model="selectedRow"
            @change="checkboxHandler(props.item)"
            primary
            hide-details
          ></v-checkbox>
        </td>
        <td>{{ props.item.id }}</td>
        <td>{{ props.item.albumId }}</td>
        <td class="text-xs-right">{{ props.item.title }}</td>
        <td class="text-xs-right">{{ props.item.url }}</td>
        <td class="text-xs-right">{{ props.item.thumbnailUrl }}</td>

        <!-- </tr> -->
      </template>

      <template v-slot:no-results>
        <v-alert
          :value="true"
          color="error"
          icon="warning"
        >Your search for "{{ search }}" found no results.</v-alert>
      </template>
    </v-data-table>

    <div class="text-xs-center pt-2 md4 lg4">
      <!-- I removed v-model and added @input and :value -->
      <v-pagination
        @input="paginationChangeHandler"
        :value="pagination.page"
        :length="pages"
        :total-visible="7"
        circle
      ></v-pagination>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      selectedRow: undefined,

      search: "",
      loading: false,
      // i set default totalItems and page here, this fixed a lot of strange behaviour
      pagination: { totalItems: 200, rowsPerPage: 10, page: 1 },
      data: [],
      expand: false,
      selected: [],
      headers: [
        { text: "Id", value: "id" },
        {
          text: "Album",
          align: "left",
          sortable: false,
          value: "albumId"
        },
        { text: "Title", value: "title" },
        { text: "URL", value: "url" },
        { text: "Thumbnail", value: "thumbnailUrl" }
      ]
    };
  },

  computed: {
    pages() {
      if (
        this.pagination.rowsPerPage == null ||
        this.pagination.totalItems == null
      ) {
        return 0;
      }

      return Math.ceil(
        this.pagination.totalItems / this.pagination.rowsPerPage
      );
    }
  },

  methods: {
    checkboxHandler(props) {
      // do your logic here to fetch data for your modal
      console.log(props);
    },
    // i added this (gets called on pagination components)
    paginationChangeHandler(pageNumber) {
      this.pagination.page = pageNumber;
      this.getData();
    },

    getData() {
      let url = `https://jsonplaceholder.typicode.com/photos? \n
        _limit= ${this.pagination.rowsPerPage}\n
        &_start=${this.pagination.page}`;

      // if you use es6 arrow function you dont need to do that = this.
      // this will work inside the function
      axios.get(url).then(response => {
        this.setData(response);
      });
    },
    setData(response) {
      this.data = response.data;
      // unless this.pagination.totalItems changes
      // on requests, you dont need to set it here.
      // I set it up in vues data method.
      // You can remove all these comments :)
      // this.pagination.totalItems = 200;
    }
  },
  mounted() {
    this.getData();
  }
};
</script>


