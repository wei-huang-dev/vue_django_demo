<style>
@import '../assets/styles/app.css';
</style>

<template>
<v-container fluid>

    <v-expansion-panels focusable>
        <v-expansion-panel>
            <v-expansion-panel-header>Filters</v-expansion-panel-header>
            <v-expansion-panel-content>
                <v-row>
                    <v-col class="ml-10">
                        <v-combobox v-model="state" :items="states" label="State" multiple outlined dense></v-combobox>
                    </v-col>
                    <v-col class="mr-10">
                        <v-combobox v-model="county" :items="counties" label="County" multiple outlined dense></v-combobox>
                    </v-col>
                    <v-col class="mr-10">
                        <v-combobox v-model="town" :items="towns" label="Town" multiple outlined dense></v-combobox>
                    </v-col>
                    <v-col class="mr-10">
                        <v-combobox v-model="model" :items="models" label="Model" multiple outlined dense></v-combobox>
                    </v-col>
                    <v-col class="mr-10">
                        <v-combobox v-model="color" :items="colors" label="Color" multiple outlined dense></v-combobox>
                    </v-col>
                </v-row>
            </v-expansion-panel-content>
        </v-expansion-panel>

        <v-expansion-panel>
            <v-expansion-panel-header>Group By</v-expansion-panel-header>
            <v-expansion-panel-content>
                <v-row>
                    <v-col class="ml-10">
                        <v-checkbox v-model="stateX" :label="`State`"></v-checkbox>
                    </v-col>
                    <v-col>
                        <v-checkbox v-model="countyX" :label="`County`"></v-checkbox>
                    </v-col>
                    <v-col>
                        <v-checkbox v-model="townX" :label="`Town`"></v-checkbox>
                    </v-col>
                </v-row>
            </v-expansion-panel-content>
        </v-expansion-panel>

    </v-expansion-panels>

    <v-card hover class="my-3">
        <v-row>
            <v-col class="ml-5">
                <v-checkbox v-model="fields" id="field1" value="Field 1" :label="`Field 1`"></v-checkbox>
            </v-col>
            <v-col>
                <v-checkbox v-model="fields" id="field2" value="Field 2" :label="`Field 2`"></v-checkbox>
            </v-col>
            <v-col>
                <v-checkbox v-model="fields" id="field3" value="Field 3" :label="`Field 3`"></v-checkbox>
            </v-col>
            <v-col>
                <v-checkbox v-model="fields" id="field4" value="Field 4" :label="`Field 4`"></v-checkbox>
            </v-col>
            <v-col>
                <v-checkbox v-model="fields" id="field5" value="Field 5" :label="`Field 5`"></v-checkbox>
            </v-col>
        </v-row>
        <!-- <div>Selected fields: {{ fields }}</div> -->
    </v-card>
    <v-card hover class="my-3">
        <v-row align="center">
            <v-col class="ml-5" align="center">
                ABC
            </v-col>
            <v-col cols="8">

                <v-simple-table height="300px" class='header-text-color'>
                    <template v-slot:default>
                        <thead class='header-text-color'>
                            <tr>
                                <th class="text-left">
                                    FIELD
                                </th>
                                <th class="text-left">
                                    06/01/2022
                                </th>
                                <th class="text-left">
                                    06/02/2022
                                </th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="item in fields">
                                <td>{{ item }}</td>
                                <td>xxx</td>
                                <td>yyy</td>
                                <!-- <td>{{ item.date[0] }}</td>
                                <td>{{ item.date[1] }}</td> -->
                            </tr>
                        </tbody>
                    </template>
                </v-simple-table>

            </v-col>
            <v-col class="ml-5" align="center">
                <v-row align="center">
                    <v-btn>Copy</v-btn>
                </v-row>
                <div class="my-5"></div>
                <v-row>
                    <v-btn>
                        Copy & Edit
                    </v-btn>
                </v-row>
            </v-col>
        </v-row>
    </v-card>
    <!-- <v-card hover class="my-3">
        <v-row align="center">
            <v-col class="ml-5" align="center">
                DEF
            </v-col>
            <v-col cols="8">

                <v-simple-table height="300px" class="header-text-color">
                    <template v-slot:default>
                        <thead class='header-text-color'>
                            <tr>
                                <th class="text-left">
                                    FIELD
                                </th>
                                <th class="text-left">
                                    06/01/2022
                                </th>
                                <th class="text-left">
                                    06/02/2022
                                </th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="item in fields" :key="item.id">
                                <td>{{ item.id }}</td>
                                <td>{{ item.date[0] }}</td>
                                <td>{{ item.date[1] }}</td>
                            </tr>
                        </tbody>
                    </template>
                </v-simple-table>

            </v-col>
            <v-col class="ml-5" align="center">
                <v-row align="center">
                    <v-btn>Copy</v-btn>
                </v-row>
                <div class="my-5"></div>
                <v-row>
                    <v-btn>
                        Copy & Edit
                    </v-btn>
                </v-row>
            </v-col>
        </v-row>
    </v-card> -->
</v-container>
</template>

<script>
export default {
    data() {
        return {
            checkedNames: [],
            stateX: true,
            countyX: false,
            townX: false,
            state: [],
            states: [
                'State 1',
                'State 2',
            ],
            county: [],
            counties: [
                'county 1',
                'county 2',
            ],
            town: [],
            towns: [
                'town 1',
                'town 2',
            ],
            model: [],
            models: [
                'model 1',
                'model 2',
            ],
            color: [],
            colors: [
                'color 1',
                'color 2',
            ],

            field1: false,
            field2: false,
            field3: false,
            field4: false,
            field5: false,
            idNum: 0,
            // table
            fields: [],
            fieldS: [{
                    id: 'Field 1',
                    date: ['aaa', 'bbb'],
                },
                {
                    id: 'Field 2',
                    date: ['aaa', 'bbb'],
                },
                {
                    id: 'Field 3',
                    date: ['aaa', 'bbb'],
                },
                {
                    id: 'Field 4',
                    date: ['aaa', 'bbb'],
                },
                {
                    id: 'Field 5',
                    date: ['aaa', 'bbb'],
                },
            ],
        }
    },
    methods: {
        // later
        addField() {
            console.log("add")
            let newField = {
                id: this.idNum++,
                date: ['aaa', 'bbb']

            }
            this.fields.push(newField)
        },
        deleteField(id) {
            this.fields = this.fields.filter(field => field.id !== id)
        }

    }
}
</script>
