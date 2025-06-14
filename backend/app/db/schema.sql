-- Users table (tenant-aware)
CREATE TABLE users (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  email TEXT UNIQUE NOT NULL,
  full_name TEXT,
  company_name TEXT,
  created_at TIMESTAMP DEFAULT NOW()
);

-- Cloud accounts linked to users
CREATE TABLE cloud_accounts (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID REFERENCES users(id) ON DELETE CASCADE,
  provider TEXT NOT NULL CHECK (provider IN ('aws', 'azure', 'gcp')),
  account_name TEXT,
  credentials JSONB,
  connected_at TIMESTAMP DEFAULT NOW()
);

-- Discovered secrets per cloud account
CREATE TABLE secrets (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  cloud_account_id UUID REFERENCES cloud_accounts(id) ON DELETE CASCADE,
  name TEXT NOT NULL,
  path TEXT,
  risk_score INTEGER DEFAULT 0,
  last_rotated TIMESTAMP,
  detected_at TIMESTAMP DEFAULT NOW()
);

-- Logs for scan job executions
CREATE TABLE scan_logs (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  cloud_account_id UUID REFERENCES cloud_accounts(id) ON DELETE CASCADE,
  status TEXT CHECK (status IN ('pending', 'completed', 'failed')),
  started_at TIMESTAMP DEFAULT NOW(),
  finished_at TIMESTAMP,
  error TEXT
);

-- Indexes for performance
CREATE INDEX idx_user_email ON users(email);
CREATE INDEX idx_provider ON cloud_accounts(provider);
CREATE INDEX idx_secret_name ON secrets(name);
CREATE INDEX idx_scan_status ON scan_logs(status);
