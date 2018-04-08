module.exports = function (app) {
    app.use('/api/v1/reports', require('./reports/sample'));
}