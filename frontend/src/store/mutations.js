export default {
  receivePaginatedPaintings(state, paintings) {
    const { results, count, next, previous } = paintings

    state.paintings.data = results
    state.paintings.count = count
    state.paintings.paginator.next = next
    state.paintings.paginator.previous = previous
  },

  receivePaginatedCreators(state, creators) {
    const { results, count, next, previous } = creators

    state.creators.data = results
    state.creators.count = count
    state.creators.paginator.next = next
    state.creators.paginator.previous = previous
  },

  receivePaginatedMaterials(state, materials) {
    const { results, count, next, previous } = materials

    state.materials.data = results
    state.materials.count = count
    state.materials.paginator.next = next
    state.materials.paginator.previous = previous
  },

  receivePaginatedDepicts(state, depicts) {
    const { results, count, next, previous } = depicts

    state.depicts.data = results
    state.depicts.count = count
    state.depicts.paginator.next = next
    state.depicts.paginator.previous = previous
  },

  receivePaginatedMovements(state, movements) {
    const { results, count, next, previous } = movements

    state.movements.data = results
    state.movements.count = count
    state.movements.paginator.next = next
    state.movements.paginator.previous = previous
  },
}
