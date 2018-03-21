const os = require('os')
const Speex = require('bindings')('Speex.node');

module.exports = Speex;

module.exports.NARROW_BAND = 0;
module.exports.WIDE_BAND = 1;
module.exports.ULTRA_WIDE_BAND = 2;
