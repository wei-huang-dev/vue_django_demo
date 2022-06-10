<template>
  <v-app>
    <v-data-table
      :headers="headers"
      :items="desserts"
      :items-per-page="5"
      class="elevation-1"
    >
    </v-data-table>
    <v-container>
      <v-dialog v-model="dialog" persistent max-width="900px">
        <template v-slot:activator="{ on, attrs }">
          <v-btn color="primary" dark v-bind="attrs" v-on="on">
            Add New Entry
          </v-btn>
        </template>
        <v-card>
          <v-card-title>
            <span class="text-h5">New Entry Form</span>
          </v-card-title>
          <v-card-text>
            <v-container>
              <v-row>
                <v-col>
                  <v-select
                    :items="['Thing 1', 'Thing 2', 'Thing 3']"
                    label="Classification 1*"
                    required
                    dense
                  ></v-select>
                </v-col>
                <v-col>
                  <v-select
                    :items="['Thing 1', 'Thing 2', 'Thing 3']"
                    label="Classification 2*"
                    required
                    dense
                  ></v-select>
                </v-col>
                <v-col>
                  <v-select
                    :items="['Thing 1', 'Thing 2', 'Thing 3']"
                    label="Classification 3*"
                    required
                    dense
                  ></v-select>
                </v-col>
              </v-row>
              <v-divider></v-divider>
              <v-row>
                <v-spacer></v-spacer>
                <v-col>
                  <v-select
                    :items="['Thing 1', 'Thing 2', 'Thing 3']"
                    label="Main Dropdown 1*"
                    required
                    dense
                  ></v-select>
                  <v-select
                    :items="['Thing 1', 'Thing 2', 'Thing 3']"
                    label="Main Dropdown 2*"
                    required
                    dense
                  ></v-select>
                  <v-select
                    :items="['Thing 1', 'Thing 2', 'Thing 3']"
                    label="Main Dropdown 3*"
                    required
                    dense
                  ></v-select>
                  <v-select
                    :items="['Thing 1', 'Thing 2', 'Thing 3']"
                    label="Main Dropdown 4*"
                    required
                    dense
                  ></v-select>
                  <v-checkbox
                    v-model="inport"
                    label="Inport?*"
                    required
                    dense
                  ></v-checkbox>
                </v-col>
                <v-spacer></v-spacer>
              </v-row>
              <v-row>
                <template v-if="inport">
                  <v-col>
                    <v-select
                      :items="['Thing 1', 'Thing 2', 'Thing 3']"
                      label="Inport Dropdown 1*"
                      required
                      dense
                    ></v-select>
                    <v-select
                      :items="['Thing 1', 'Thing 2', 'Thing 3']"
                      label="Inport Dropdown 2*"
                      required
                      dense
                      multiple
                    ></v-select>
                  </v-col>
                  <v-col>
                    <v-select
                      :items="['Thing 1', 'Thing 2', 'Thing 3']"
                      label="Inport Dropdown 3*"
                      required
                      dense
                    ></v-select>
                    <v-select
                      :items="['Thing 1', 'Thing 2', 'Thing 3']"
                      label="Inport Dropdown 4*"
                      required
                      dense
                    ></v-select>
                  </v-col>
                </template>
                <template v-else>
                  <v-col>
                    <v-select
                      :items="['Thing 1', 'Thing 2', 'Thing 3']"
                      label="Outport Dropdown 1*"
                      required
                      dense
                    ></v-select>
                  </v-col>
                  <v-col>
                    <v-select
                      :items="['Thing 1', 'Thing 2', 'Thing 3']"
                      label="Outport Dropdown 1*"
                      required
                      dense
                    ></v-select>
                  </v-col>
                  <v-col>
                    <v-select
                      :items="['Thing 1', 'Thing 2', 'Thing 3']"
                      label="Outport Dropdown 1*"
                      required
                      dense
                    ></v-select>
                  </v-col>
                </template>
              </v-row>
              <v-row>
                <v-col>
                  <v-textarea
                    outlined
                    clearable
                    clear-icon="mdi-close-circle"
                    label="Comment Box"
                  ></v-textarea>
                </v-col>
                <v-checkbox
                  v-model="publish"
                  label="Publish?"
                  dense
                ></v-checkbox>
              </v-row>
              <v-row>
                <v-col>
                  <v-select
                      :items="['Thing 1', 'Thing 2', 'Thing 3']"
                      label="Bottom Dropdown 1*"
                      required
                      dense
                    ></v-select>
                </v-col>
                <v-col>
                  <v-select
                      :items="['Thing 1', 'Thing 2', 'Thing 3']"
                      label="Bottom Dropdown 2*"
                      required
                      dense
                    ></v-select>
                </v-col>
                <v-col>
                  <v-select
                      :items="['Thing 1', 'Thing 2', 'Thing 3']"
                      label="Bottom Dropdown 3*"
                      required
                      dense
                    ></v-select>
                </v-col>
              </v-row>
            </v-container>
            <small>*indicates required field</small>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="blue darken-1" text @click="dialog = false">
              Close
            </v-btn>
            <v-btn color="blue darken-1" text @click="dialog = false">
              Save
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-container>
  </v-app>
</template>

<script>
export default {
  data() {
    return {
      dialog: false,
      inport: true,
      publish: false,
      headers: [
        {
          text: "Dessert (100g serving)",
          align: "start",
          sortable: false,
          value: "name",
        },
        { text: "Calories", value: "calories" },
        { text: "Fat (g)", value: "fat" },
        { text: "Carbs (g)", value: "carbs" },
        { text: "Protein (g)", value: "protein" },
        { text: "Iron (%)", value: "iron" },
      ],
      desserts: [
        {
          name: "Frozen Yogurt",
          calories: 159,
          fat: 6.0,
          carbs: 24,
          protein: 4.0,
          iron: "1%",
        },
        {
          name: "Ice cream sandwich",
          calories: 237,
          fat: 9.0,
          carbs: 37,
          protein: 4.3,
          iron: "1%",
        },
        {
          name: "Eclair",
          calories: 262,
          fat: 16.0,
          carbs: 23,
          protein: 6.0,
          iron: "7%",
        },
        {
          name: "Cupcake",
          calories: 305,
          fat: 3.7,
          carbs: 67,
          protein: 4.3,
          iron: "8%",
        },
        {
          name: "Gingerbread",
          calories: 356,
          fat: 16.0,
          carbs: 49,
          protein: 3.9,
          iron: "16%",
        },
        {
          name: "Jelly bean",
          calories: 375,
          fat: 0.0,
          carbs: 94,
          protein: 0.0,
          iron: "0%",
        },
        {
          name: "Lollipop",
          calories: 392,
          fat: 0.2,
          carbs: 98,
          protein: 0,
          iron: "2%",
        },
        {
          name: "Honeycomb",
          calories: 408,
          fat: 3.2,
          carbs: 87,
          protein: 6.5,
          iron: "45%",
        },
        {
          name: "Donut",
          calories: 452,
          fat: 25.0,
          carbs: 51,
          protein: 4.9,
          iron: "22%",
        },
        {
          name: "KitKat",
          calories: 518,
          fat: 26.0,
          carbs: 65,
          protein: 7,
          iron: "6%",
        },
      ],
    };
  },
};
</script>

<style></style>
