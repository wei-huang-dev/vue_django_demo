<template>
<v-card hover class="my-3">
    <v-card-title class="ml-3">
        <span>{{ title }}</span>
    </v-card-title>
    <v-row align="center">
        <v-col cols="8">
            <v-simple-table height="300px" fixed-header id="fieldTable">
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
                        <tr v-for="(item, index) in selectedFields">
                            <td>{{ item }}</td>
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
</template>

<script>
export default {
    props: {
        title: String,
        selectedFields: []
    },
    data() {
        return {
            dates: [
                new Date(new Date().getTime() - 86400000).toLocaleDateString(),
                new Date().toLocaleDateString()
            ],

            fieldData: [
                'xxx',
                'yyy',
            ],

            newDate: 0,
            lastDate: new Date(),
            newDate: new Date(),
            idNum: 0,
        }
    },
    methods: {
        copyLastDate() {
            this.newDate = new Date(this.lastDate.getTime() + 86400000); // (24 * 60 * 60 * 1000)
            this.dates.push(this.newDate.toLocaleDateString());
            this.lastDate = this.newDate;
            this.fieldData.push(this.fieldData[this.fieldData.length - 1]);
        },
    }
}
</script>
