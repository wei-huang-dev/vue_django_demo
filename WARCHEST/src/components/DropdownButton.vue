<template>
<div class="text-center">
    <v-menu offset-y>
        <template v-slot:activator="{ on, attrs }">
            <v-btn color="primary" dark v-bind="attrs" v-on="on">Copy
            </v-btn>
        </template>
        <v-list>
            <v-list-item v-for="(item, index) in items" :key="index" @click="$emit('tableTitle', index)">
                <v-list-item-title>{{ item }}</v-list-item-title>
            </v-list-item>
        </v-list>
    </v-menu>
</div>
</template>

<script>
export default {
    data: () => ({
        items: [
            'ABC',
            'DEF',
            'GIJ',
            'KLM'
        ],
    }),
    methods: {
        handleClick(index) {
            // alert(index + "454")
            
            // this.newDate = new Date(this.lastDate.getTime() + 86400000); // (24 * 60 * 60 * 1000)
            // this.dates.push(this.newDate.toLocaleDateString());
            // this.lastDate = this.newDate;
            // this.fieldData.push(this.fieldData[this.fieldData.length - 1]);
        },
    },
}
</script>
