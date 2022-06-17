<style>
@import '../assets/app.css';
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
    </v-card>
    <div>
        <!-- Selected fields: {{ fields }} -->
        <!-- {{new Date().toLocaleDateString() | formatDate}} -->
    </div>
    <v-card hover class="my-3">
        <v-card-title class="ml-3">
            <h5>ABC</h5>
        </v-card-title>
        <v-row align="center">
            <v-col cols="10">
                <v-simple-table class="ml-5" id="fieldTable">
                    <template v-slot:default>
                        <thead>
                            <tr>
                                <th class="text-left">
                                    FIELD
                                </th>
                                <th class="text-left" v-for="item in dates">
                                    {{ item }}
                                </th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="(item, index)  in fields">
                                <th>{{ item }}</th>
                                <td v-for="fItem in fieldData">
                                    {{item.slice(-1)}}{{fItem}}
                                </td>
                            </tr>
                        </tbody>
                    </template>
                </v-simple-table>
            </v-col>
            <v-col class="ml-5" align="center">
                <v-row align="center">
                    <v-btn @click="copyLastDate()">Copy</v-btn>
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
</v-container>
</template>

<script>
export default {
    data() {
        return {
            id: 0,
            checkedNames: [],
            stateX: true,
            countyX: false,
            townX: false,
            state: [],
            states: [
                'State 1',
                'State 2',
                'State 31',
                'State 42',
                'State 51',
                'State 62',
                'State 71',
                'State 82',
                'State 91',
                'State 14',
                'State 21',
                'State 31',
                'State 26',
                'State 18',
                'State 26',
                'State 19',
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

            dates: [
                new Date(new Date().getTime() - 86400000).toLocaleDateString(),
                new Date().toLocaleDateString()
            ],

            fieldData: [
                'xxx',
                'yyy',
            ],

            field1: false,
            field2: false,
            field3: false,
            field4: false,
            field5: false,

            newDate: 0,
            lastDate: new Date(),
            newDate: new Date(),
            idNum: 0,
            // table
            fields: [],
        }
    },
    methods: {
        copyLastDate() {
            this.newDate = new Date(this.lastDate.getTime() + 86400000); // (24 * 60 * 60 * 1000)
            this.dates.push(this.newDate.toLocaleDateString());
            this.lastDate = this.newDate;
            this.fieldData.push(this.fieldData[this.fieldData.length - 1]);
        },
        // later
        copyLastDate1() {
            this.newDate = this.dates.length + 1;
            this.dates.push('Date ' + this.newDate);
            this.fieldData.push(this.fieldData[this.fieldData.length - 1]);
        },
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
        },
        format_date(value) {
            if (value) {
                return moment(String(value)).format('YYYYMMDD')
            }
        }
    }
}
</script>
