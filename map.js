const wards = require('./wards.json');
const token = require('./env.json');
let map;
$(window).on("load", function() {
    "use strict";
    const ward = wards.features;
    const maps = {
        'total': 'mapbox://styles/omerfarooqahmed/ck2ha3hy91rh91dmtqxv6tvuj',
        'male': 'mapbox://styles/omerfarooqahmed/ck2ha72tp0sdq1cs2qhy2ssdy',
        'female': 'mapbox://styles/omerfarooqahmed/ck2ha99x21rmh1dmtvawh80ng'
    }
    $.getScript('https://api.tiles.mapbox.com/mapbox-gl-js/v1.5.0/mapbox-gl.js', function() {
        mapboxgl.accessToken = token.API;
        map = new mapboxgl.Map({
            container: 'map',
            style: maps[document.getElementById('mapname')],
            center: [0.1278, 51.5074],
            zoom: 10
        });
        const addWard = (data) => {
            map.addLayer({
               'id': `${data.properties.wd16cd}`,
               'type': 'fill',
                'source': {
                    'type': 'geojson',
                    'data': {
                        'type': 'Feature',
                        'geometry': {
                            'type': 'Polygon',
                            'coordinates': data.geometry.coordinates
                        }
                    }
                },
                'layout': {},
                'paint': {
                    'fill-color': '#ff00d4',
                    'fill-opacity': 0.8
                }
            })
        }

        map.on('mousemove', function(e) {
            var states = map.queryRenderedFeatures(e.point, {
                layers: ['result2-0qiqd7']
            });

            if (states.length>0) {
                document.getElementById('pd').innerHTML = '<h3><strong>' +
                states[0].properties.wd16nm + '</strong></h3><p><strong><em>' +
                states[0].properties.total_value + '</strong> Number of Claimants</em></p>';
            } else {
                document.getElementById('pd').innerHTML = '<p>Hower over a ward!</P>';
            }
        });
    });
  });