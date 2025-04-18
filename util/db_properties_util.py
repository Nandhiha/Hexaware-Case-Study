import configparser


def get_db_config():
    config = configparser.ConfigParser()
    
    
    config.read('db_config.ini')
    
    db_config = {
        'driver': config.get('database', 'driver'),
        'server': config.get('database', 'server'),
        'database': config.get('database', 'database'),
        'trusted_connection': config.get('database', 'trusted_connection')
    }
    
    return db_config


def get_connection_string():
    db_config = get_db_config()
    conn_str = (
        f"Driver={db_config['driver']};"
        f"Server={db_config['server']};"
        f"Database={db_config['database']};"
        f"Trusted_Connection={db_config['trusted_connection']};"
    )
    return conn_str
