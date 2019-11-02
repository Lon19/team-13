(function(){function r(e,n,t){function o(i,f){if(!n[i]){if(!e[i]){var c="function"==typeof require&&require;if(!f&&c)return c(i,!0);if(u)return u(i,!0);var a=new Error("Cannot find module '"+i+"'");throw a.code="MODULE_NOT_FOUND",a}var p=n[i]={exports:{}};e[i][0].call(p.exports,function(r){var n=e[i][1][r];return o(n||r)},p,p.exports,r,e,n,t)}return n[i].exports}for(var u="function"==typeof require&&require,i=0;i<t.length;i++)o(t[i]);return o}return r})()({1:[function(require,module,exports){
module.exports={
    "API": "pk.eyJ1Ijoib21lcmZhcm9vcWFobWVkIiwiYSI6ImNrMmdsdmk5ajB0dWEzaXBiY3N0eHMzbGoifQ._zfITRMXwnQQ4Inor_VCQA"
}
},{}],2:[function(require,module,exports){
const wards = require('./wards.json');
// const token = require('../env.json');
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
        mapboxgl.accessToken = 'pk.eyJ1Ijoib21lcmZhcm9vcWFobWVkIiwiYSI6ImNrMmdsdmk5ajB0dWEzaXBiY3N0eHMzbGoifQ._zfITRMXwnQQ4Inor_VCQA';
        console.log('this', document.getElementById('map_django').attributes.name.nodeValue);
        map = new mapboxgl.Map({
            container: 'map',
            style: maps[document.getElementById('map_django').attributes.name.nodeValue],
            center: [0.1278, 51.5074],
            zoom: 10
        });
        console.log(maps[document.getElementById('map_django').attributes.name.nodeValue]);
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

        document.getElementById('button').onclick = () => {
          console.log('this', document.getElementById('postcode'));
        }
    });
  });
},{"./env.json":1,"./wards.json":3}],3:[function(require,module,exports){},{}]},{},[2]);
