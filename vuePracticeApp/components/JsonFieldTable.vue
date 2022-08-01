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
                <v-btn color="primary" @click="apply">Apply</v-btn>
            </v-col>
        </v-row>

    </v-card>
    <v-card hover class="my-3">
        <v-row align="center">
            <v-col cols="10">

                <v-data-table :headers="headers" :items="items" dense disable-sort item-key="id" group-by="title">
                    <template v-slot:group.header="{items, isOpen, toggle}">
                        <th colspan="20">
                            <v-icon @click="toggle">{{ isOpen ? 'mdi-minus' : 'mdi-plus' }}
                            </v-icon>
                            {{ items[0].title }}
                        </th>
                    </template>
                    <template v-slot:item="{ item }">
                        <tr>
                            <td v-for="(header, index) in headers">
                                <span v-if="index">{{ item.cols[index-1] }}</span>
                                <span v-else>{{ item.name }}</span>
                            </td>
                        </tr>
                    </template>
                </v-data-table>
            </v-col>
            <v-col class="ml-5" align="center">
                <!-- <v-row>
                    <v-btn color="primary" @click="refresh">Refresh</v-btn>
                </v-row> -->
                <div class="my-5"></div>
                <v-row>
                    <dropdownButton @tableTitle="getTitle" />
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
</container>
</template>

<script>
export default {

    data() {
        return {
            fields: ["Field 1", "Field 2", "Field 3", "Field 4", "Field 5"],
            jsonData: {
                "dates": ["7/27/2022", "7/28/2022"],
                "tables": [{
                        "title": "ABC",
                        "fieldData": [
                            [10, 20],
                            [11, 21],
                            [12, 22],
                            [13, 23],
                            [13, 23]
                        ]
                    },
                    {
                        "title": "DEF",
                        "fieldData": [
                            [10, 20],
                            [11, 21],
                            [32, 22],
                            [13, 23],
                            [13, 23]
                        ]
                    },
                    {
                        "title": "GIJ",
                        "fieldData": [
                            [10, 20],
                            [11, 21],
                            [42, 22],
                            [13, 23],
                            [13, 23]
                        ]
                    },
                    {
                        "title": "KLM",
                        "fieldData": [
                            [10, 20],
                            [11, 21],
                            [52, 22],
                            [13, 23],
                            [13, 23]
                        ]
                    },
                ]
            },
            obj: null,
            responseData: null,
            index: 0,
            headers: [],
            items: [],

            lastDate: new Date(),
            newDate: new Date(),

            tableTitles: [
                'ABC',
                'DEF',
                'GIJ',
                'KLM',
            ],
        }
    },
    mounted() {
        this.index = this.headers.length
        this.refresh()
    },
    methods: {
        refresh() {

            // axios.get('https://api.coindesk.com/v1/bpi/historical/close.json?start=2013-09-01&end=2013-09-05').then(response => {
            //     this.responseData = response.data.bpi;

            this.responseData = this.jsonData

            this.headers = [{
                text: 'TITLE_FIELD',
                class: 'style-1'

            }]

            for (let j = 0; j < this.responseData.dates.length; j++) {
                this.headers.push({
                    text: this.responseData.dates[j],
                    class: 'style-1'

                })
            }

            this.apply()

        },

        copy(title) {
            let items = this.responseData.tables
            let itemsLen = 0
            let headersLen = this.headers.length - 1

            for (let i = 0; i < items.length; i++) {

                if (items[i].title === title) {
                    console.log(items[i].title)
                    items[i].fieldData.forEach(fieldItem => {
                        fieldItem.push(fieldItem[fieldItem.length - 1])
                    })
                    itemsLen = items[i].fieldData[0].length
                    console.log(itemsLen)
                }
            }
            console.log(headersLen)
            if (headersLen < itemsLen) {
                this.newDate = new Date(this.lastDate.getTime() + 86400000); // (24 * 60 * 60 * 1000)
                this.headers.push({
                    text: this.newDate.toLocaleDateString(),
                    class: 'style-1'

                });
                this.lastDate = this.newDate;
            }
        },

        apply() {

            this.items = []

            let fieldData = null
            for (let i = 0; i < this.responseData.tables.length; i++) {

                this.fields.sort().forEach(field => {
                    switch (field) {
                        case 'Field 1':
                            fieldData = this.responseData.tables[i].fieldData[0];
                            break;
                        case 'Field 2':
                            fieldData = this.responseData.tables[i].fieldData[1];
                            break;
                        case 'Field 3':
                            fieldData = this.responseData.tables[i].fieldData[2];
                            break;
                        case 'Field 4':
                            fieldData = this.responseData.tables[i].fieldData[3];
                            break;
                        default:
                            fieldData = this.responseData.tables[i].fieldData[4];
                    }

                    this.items.push({
                        title: this.responseData.tables[i].title,
                        name: field,
                        cols: fieldData
                    })

                })

            }
        },

        getTitle(titleIndex) {
            this.copy(this.tableTitles[titleIndex]);
        }
    },

    components: {
        'dropdownButton': require('@/components/DropdownButton.vue').default,
    }
}
</script>
