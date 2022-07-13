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
    </v-card>
    <fieldTable title="ABC" :selectedFields="fields" />
    <fieldTable title="DEF" :selectedFields="fields" />
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

            lastDate: new Date(),
            newDate: new Date(),

            fields: ["Field 1", "Field 2", "Field 3", "Field 4", "Field 5"],
        }
    },
    methods: {
        copyLastDate() {
            this.newDate = new Date(this.lastDate.getTime() + 86400000); // (24 * 60 * 60 * 1000)
            this.dates.push(this.newDate.toLocaleDateString());
            this.lastDate = this.newDate;
            this.fieldData.push(this.fieldData[this.fieldData.length - 1]);
        },
        format_date(value) {
            if (value) {
                return moment(String(value)).format('YYYYMMDD')
            }
        }
    }
}
</script>
