<template>
<container>
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
            <v-col>
                <dropdownButton @tableTitle="getTitle" />
            </v-col>
            <v-col>
                <editButton>
                    Edit
                </editButton>
            </v-col>
            <v-col>
                <exportDropdownButton @exportType="getExportType" />
            </v-col>
            <v-col>
                <v-btn :loading="loading" :disabled="loading" color="primary" class="white--text" @click="loader=false">
                    <v-icon dark>
                        mdi-refresh
                    </v-icon>
                </v-btn>
            </v-col>

        </v-row>
    </v-card>

    <v-card hover class="my-3">
        <v-row align="center">
            <v-col cols="10">
                <section v-if="errored">
                    <p>Sorry - {{errorMsg}}</p>
                </section>
                <section v-else>
                    <!-- loading check can be disabled to keep existing data on the display -->
                    <div align="center" v-if="loading">
                        <v-progress-circular indeterminate color="blue-grey" size="90">
                            Loading...
                        </v-progress-circular>
                    </div>
                    <div v-else class="scrollsettings">
                        <v-simple-table height="100%" width="100%" id="fieldTable">
                            <template v-slot:default>
                                <thead>
                                    <tr>
                                        <th class="headcol">
                                            DATE
                                        </th>
                                        <th class="text-left" v-for="item in dates">
                                            {{ item }}
                                        </th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <template v-for="(titem, tindex) in tableTitles">
                                        <tr>
                                            <td class="headcol" bgcolor=#eef>{{titem}}</td>
                                            <td bgcolor=#eef v-for="fItem in dates">
                                            </td>
                                        </tr>
                                        <tr v-for="(item, index) in fields.sort()">
                                            <td class="headcol" bgcolor=#efe>{{ item }}</td>
                                            <td v-for="fItem in fieldTables[tindex][index]">
                                                {{fItem}}
                                            </td>
                                        </tr>
                                    </template>
                                </tbody>
                            </template>
                        </v-simple-table>
                    </div>
                </section>
            </v-col>
        </v-row>
    </v-card>
</container>
</template>

<script>
import axios from "axios";
import moment from 'moment';
import Globals from "../Globals";
import {
    fileTypeParser
} from "../helpers/fileTypeParser";

export default {
    data() {
        return {
            loading: true,
            loader: null,
            errored: false,
            errorMsg: "",
            fields: ["Field 1", "Field 2", "Field 3", "Field 4", "Field 5"],

            warchestData: [],

            dates: [
                new Date(new Date().getTime() - 86400000).toLocaleDateString(),
                new Date().toLocaleDateString()
            ],

            tableTitles: [
                'ABC',
                'DEF',
                'GIJ',
                'KLM',
            ],

            fieldTables: [],
            lastDate: new Date(),
            newDate: new Date(),
            selectedCopy: "",
            exportType: "xls",
        }
    },

    watch: {
        loader() {
            this.loader = null
            this.refreshData()
        },
    },
    mounted() { // front end preset data

        this.dates[0] = this.formatDate(this.dates[0])
        this.dates[1] = this.formatDate(this.dates[1])

        this.fieldTables.push([
            ['a1', 'b1'],
            ['a2', 'b2'],
            ['a3', 'b3'],
            ['a4', 'b4'],
            ['a5', 'b5']
        ]) // table AB (date range)
        this.fieldTables.push([
            ['d1', 'e1'],
            ['d2', 'e2'],
            ['d3', 'e3'],
            ['d4', 'e4'],
            ['d5', 'e5']
        ]) // table DE
        this.fieldTables.push([
            ['g1', 'i1'],
            ['g2', 'i2'],
            ['g3', 'i3'],
            ['g4', 'i4'],
            ['g5', 'i5']
        ])
        this.fieldTables.push([
            ['a1', 'b1'],
            ['a2', 'b2'],
            ['a3', 'b3'],
            ['a4', 'b4'],
            ['a5', 'b5']
        ])
        this.loading = false // display preset data
    },
    methods: {
        formatDate(value) {
            if (value) {
                return moment(String(value)).format('YYMMDD')
            }
        },
        async refreshData() {
            this.loading = true
            Globals.countryCode = Globals.US_CODE
            console.log("refresh data..." + Globals.countryCode)
            let field1 = []
            let field2 = []
            let field3 = []
            let field4 = []
            let field5 = []
            let tables = []
            this.fieldTables = []

            await axios.get(Globals.API_URL + "warchest")
                //            await axios.get(this.$API_URL + "warchest")
                .then((response) => {
                    this.$warchestData = response.data;
                    const jsonStr = JSON.stringify(this.$warchestData)
                    const jsObj = JSON.parse(jsonStr);

                    const dateCount = 2; // 2 dates for testing 
                    console.log('get data')
                    this.dates = []
                    this.dates.push(this.formatDate(jsObj[0]['Date']))
                    this.dates.push(this.formatDate(jsObj[1]['Date']))
                    console.log(jsObj[0]['Date'])
                    console.log(jsObj[1]['Date'])
                    console.log(this.formatDate(jsObj[0]['Date']))
                    console.log(this.formatDate(jsObj[1]['Date']))
                    this.lastDate = new Date(jsObj[1]['Date'])
                    console.log(this.lastDate) //??

                    let k = 0
                    for (let i = 0; i < jsObj.length / dateCount; i++) {
                        for (let j = 0; j < dateCount; j++) {
                            field1.push(jsObj[k]['Field1']) // table AB (date range)
                            field2.push(jsObj[k]['Field2'])
                            field3.push(jsObj[k]['Field3'])
                            field4.push(jsObj[k]['Field4'])
                            field5.push(jsObj[k]['Field5'])
                            k++
                        }
                        tables.push(field1)
                        tables.push(field2)
                        tables.push(field3)
                        tables.push(field4)
                        tables.push(field5)
                        this.fieldTables.push(tables)

                        field1 = []
                        field2 = []
                        field3 = []
                        field4 = []
                        field5 = []
                        tables = []
                    }
                    // var obj = JSON.parse(jsonStr, function (key, value) {
                    // });

                })
                .catch(error => {
                    console.log(error)
                    this.errored = true
                    this.errorMsg = error.message
                })
                .finally(() => this.loading = false)
        },

        copyLastDate(x) {
            console.log(x + '----' + this.lastDate)
            if (this.fieldTables[x][1].length == this.dates.length) {
                this.newDate = new Date(this.lastDate.getTime() + 86400000); // (24 * 60 * 60 * 1000)
                this.dates.push(this.formatDate(this.newDate.toLocaleDateString()));
                this.lastDate = this.newDate;
            }
            for (let i = 0; i < this.fieldTables[x].length; i++)
                this.fieldTables[x][i].push(this.fieldTables[x][i][this.fieldTables[x][i].length - 1]);
        },

        getTitle(titleIndex) {
            this.selectedCopy = titleIndex;
            this.copyLastDate(titleIndex);
        },

        getExportType(exportType) {
            fileTypeParser().exportDataFromJSON(this.$warchestData, "warchest-data", exportType);
        },

    },

    components: {
        'dropdownButton': require('@/components/DropdownButton.vue').default,
        'exportDropdownButton': require('@/components/ExportDropdownButton.vue').default,
        'editButton': require('@/components/EditDialog.vue').default,
    }
}
</script>
