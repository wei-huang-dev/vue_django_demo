<template>
<div class="text-center">
    <v-menu offset-y>
        <template v-slot:activator="{ on, attrs }">
            <v-btn color="primary" dark v-bind="attrs" v-on="on">Export
            </v-btn>
        </template>
        <v-list>
            <v-list-item v-for="(item, index) in items" @click="$emit('exportType', item)">
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
            'xls',
            'csv',
            'json',
            'txt'
        ],
    }),
}
</script>
