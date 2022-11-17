<template>
<v-container fluid>
<div class="text-center">
    <v-menu offset-y>
        <template v-slot:activator="{ on, attrs }">
            <v-btn color="primary" dark v-bind="attrs" v-on="on">Track
            </v-btn>
        </template>
        <v-list>
            <v-list-item v-for="(item, index) in items" :key="index" @click="$emit('tableTitle', index)">
                <v-list-item-title>{{ item }}</v-list-item-title>
            </v-list-item>
        </v-list>
    </v-menu>
</div>

<div>
    <map1 />
</div>
</v-container>
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
    components: {
        'map1': require('@/components/map.vue').default,
    }
}
</script>
