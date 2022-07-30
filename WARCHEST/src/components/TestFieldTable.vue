<template>
<div id="app">

    <v-container>
        <v-row>
            <v-btn @click="refresh">REFRESH</v-btn>
            <v-btn @click="copy">COPY</v-btn>
        </v-row>
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

    </v-container>

</div>
</template>

<script>
export default {

    props: {
        selectedFields: [],
    },
    watch: {
    },
    data() {
        return {

            jsonData: {
                "dates": ["7/27/2022", "7/28/2022"],
                "tables": [{
                        "title": "ABC",
                        "fields": [
                            [10, 20],
                            [11, 21],
                            [12, 22],
                            [13, 23],
                            [13, 23]
                        ]
                    },
                    {
                        "title": "DEF",
                        "fields": [
                            [10, 20],
                            [11, 21],
                            [32, 22],
                            [13, 23],
                            [13, 23]
                        ]
                    },
                    {
                        "title": "GIJ",
                        "fields": [
                            [10, 20],
                            [11, 21],
                            [42, 22],
                            [13, 23],
                            [13, 23]
                        ]
                    },
                    {
                        "title": "KLM",
                        "fields": [
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
        }
    },
    mounted() {
        this.index = this.headers.length
        //        this.redo = selectedFields.length
    },
    methods: {
        refresh() {

            // axios.get('https://api.coindesk.com/v1/bpi/historical/close.json?start=2013-09-01&end=2013-09-05').then(response => {
            //     this.responseData = response.data.bpi;

            this.responseData = this.jsonData

            this.headers = [{
                text: 'TITLE_FIELD',
            }]
            this.items = []

            // for (const $property in this.responseData) {
            //     // console.log($property)
            //     console.log(this.responseData[$property])

            //     console.log($property)
            //     console.log(this.responseData[$property])

            for (let j = 0; j < this.responseData.dates.length; j++) {
                this.headers.push({
                    text: this.responseData.dates[j],
                })
            }

            this.selectedFields.forEach((element, index) => {
                console.log(element + " " + index);
                if (element === 'Field 1') {
                    console.log('sdfasdfasdfas');
                }
            })

            let fieldData = null
            for (let i = 0; i < this.responseData.tables.length; i++) {

                this.selectedFields.forEach(field => {
                    switch (field) {
                        case 'Field 1':
                            fieldData = this.responseData.tables[i].fields[0];
                            break;
                        case 'Field 2':
                            fieldData = this.responseData.tables[i].fields[1];
                            break;
                        default:
                            fieldData = this.responseData.tables[i].fields[2];
                    }

                    this.items.push({
                        title: this.responseData.tables[i].title,
                        name: field,
                        cols: fieldData // check field number
                    })

                })

            }

        },

        copy() {
            let items = this.responseData.tables
            let itemsLen = 0
            let headersLen = this.responseData.dates.length

            for (let i = 0; i < items.length; i++) {
                console.log(items[i].title)
                if (items[i].title === 'ABC') {
                    itemsLen = items[i].fields[0].length
                    items[i].fields[0].push(items[i].fields[0][itemsLen - 1])
                }
            }

            if (headersLen < itemsLen) {
                this.headers.push({
                    text: this.responseData.dates[headersLen - 1],
                })
            }
        }

    }
}
</script>
