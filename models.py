#!/usr/bin/env python3
"""
Database Models for AI-Powered Email Marketing Optimizer
Comprehensive SQLAlchemy models for managing email campaigns, contacts,
analytics, automation workflows, and AI optimization data.

🗄️ **DATABASE MODELS:**
- User management and authentication
- Email campaigns and templates
- Contact management and segmentation
- A/B testing and analytics
- Automation workflows and triggers
- AI optimization data and metrics
- Integration settings and webhooks

Author: AI Marketing Team
Version: 1.0.0
License: MIT
"""

from datetime import datetime, timezone
from typing import Dict, List, Optional, Any
import json
import uuid
from enum import Enum

from flask_sqlalchemy import SQLAlchemy
