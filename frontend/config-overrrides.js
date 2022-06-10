module.exports = function override (config, env) {
    console.log('override')
    let loaders = config.resolve
    loaders.fallback = {
        "url": require.resolve("url/")
    }
    
    return config
}