asana_teams="""{
      "type": "SCHEMA",
      "stream": "teams",
      "tap_stream_id": "teams",
      "schema": {
        "type": [
          "null",
          "object"
        ],
        "additionalProperties": false,
        "properties": {
          "gid": {
            "type": [
              "null",
              "string"
            ]
          },
          "resource_type": {
            "type": [
              "null",
              "string"
            ]
          },
          "name": {
            "type": [
              "null",
              "string"
            ]
          },
          "description": {
            "type": [
              "null",
              "string"
            ]
          },
          "html_description": {
            "type": [
              "null",
              "string"
            ]
          },
          "organization": {
            "type": [
              "null",
              "object"
            ],
            "additionalProperties": false,
            "properties": {
              "gid": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "resource_type": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "name": {
                "type": [
                  "null",
                  "string"
                ]
              }
            }
          },
          "permalink_url": {
            "type": [
              "null",
              "string"
            ]
          },
          "users": {
            "type": [
              "null",
              "array"
            ],
            "items": {
              "type": [
                "null",
                "object"
              ],
              "additionalProperties": false,
              "properties": {
                "gid": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "resource_type": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "name": {
                  "type": [
                    "null",
                    "string"
                  ]
                }
              }
            }
          }
        }
      },
      "metadata": [
        {
          "breadcrumb": [],
          "metadata": {
            "table-key-properties": [
              "gid"
            ],
            "forced-replication-method": "FULL_TABLE",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "gid"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "resource_type"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "name"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "description"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "html_description"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "organization"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "permalink_url"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "users"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        }
      ],
      "key_properties": [
        "gid"
      ],
      "replication_key": null,
      "replication_method": "FULL_TABLE"
    }"""
asana_stories="""{
      "type": "SCHEMA",
      "stream": "stories",
      "tap_stream_id": "stories",
      "schema": {
        "type": [
          "null",
          "object"
        ],
        "additionalProperties": false,
        "properties": {
          "gid": {
            "type": [
              "null",
              "string"
            ]
          },
          "resource_type": {
            "type": [
              "null",
              "string"
            ]
          },
          "created_at": {
            "type": [
              "null",
              "string"
            ],
            "format": "date-time"
          },
          "created_by": {
            "type": [
              "null",
              "object"
            ],
            "additionalProperties": false,
            "properties": {
              "gid": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "resource_type": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "name": {
                "type": [
                  "null",
                  "string"
                ]
              }
            }
          },
          "resource_subtype": {
            "type": [
              "null",
              "string"
            ]
          },
          "text": {
            "type": [
              "null",
              "string"
            ]
          },
          "html_text": {
            "type": [
              "null",
              "string"
            ]
          },
          "is_pinned": {
            "type": [
              "null",
              "boolean"
            ]
          },
          "assignee": {
            "type": [
              "null",
              "object"
            ],
            "additionalProperties": false,
            "properties": {
              "gid": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "resource_type": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "name": {
                "type": [
                  "null",
                  "string"
                ]
              }
            }
          },
          "dependency": {
            "type": [
              "null",
              "object"
            ],
            "additionalProperties": false,
            "properties": {
              "gid": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "resource_type": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "name": {
                "type": [
                  "null",
                  "string"
                ]
              }
            }
          },
          "duplicate_of": {
            "type": [
              "null",
              "object"
            ],
            "additionalProperties": false,
            "properties": {
              "gid": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "resource_type": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "name": {
                "type": [
                  "null",
                  "string"
                ]
              }
            }
          },
          "duplicated_from": {
            "type": [
              "null",
              "object"
            ],
            "additionalProperties": false,
            "properties": {
              "gid": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "resource_type": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "name": {
                "type": [
                  "null",
                  "string"
                ]
              }
            }
          },
          "follower": {
            "type": [
              "null",
              "object"
            ],
            "additionalProperties": false,
            "properties": {
              "gid": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "resource_type": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "name": {
                "type": [
                  "null",
                  "string"
                ]
              }
            }
          },
          "hearted": {
            "type": [
              "null",
              "boolean"
            ]
          },
          "hearts": {
            "anyOf": [
              {
                "type": "array",
                "items": {
                  "type": [
                    "null",
                    "object"
                  ],
                  "additionalProperties": false,
                  "properties": {
                    "gid": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "user": {
                      "type": [
                        "null",
                        "object"
                      ],
                      "additionalProperties": false,
                      "properties": {
                        "gid": {
                          "type": [
                            "null",
                            "string"
                          ]
                        },
                        "resource_type": {
                          "type": [
                            "null",
                            "string"
                          ]
                        },
                        "name": {
                          "type": [
                            "null",
                            "string"
                          ]
                        }
                      }
                    }
                  }
                }
              },
              {
                "type": "null"
              }
            ]
          },
          "is_edited": {
            "type": [
              "null",
              "boolean"
            ]
          },
          "liked": {
            "type": [
              "null",
              "boolean"
            ]
          },
          "likes": {
            "anyOf": [
              {
                "type": "array",
                "items": {
                  "type": [
                    "null",
                    "object"
                  ],
                  "additionalProperties": false,
                  "properties": {
                    "gid": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "user": {
                      "type": [
                        "null",
                        "object"
                      ],
                      "additionalProperties": false,
                      "properties": {
                        "gid": {
                          "type": [
                            "null",
                            "string"
                          ]
                        },
                        "resource_type": {
                          "type": [
                            "null",
                            "string"
                          ]
                        },
                        "name": {
                          "type": [
                            "null",
                            "string"
                          ]
                        }
                      }
                    }
                  }
                }
              },
              {
                "type": "null"
              }
            ]
          },
          "new_approval_status": {
            "type": [
              "null",
              "boolean"
            ]
          },
          "new_dates": {
            "type": [
              "null",
              "object"
            ],
            "additionalProperties": false,
            "properties": {
              "due_at": {
                "type": [
                  "null",
                  "string"
                ],
                "format": "date-time"
              },
              "due_on": {
                "type": [
                  "null",
                  "string"
                ],
                "format": "date-time"
              },
              "start_on": {
                "type": [
                  "null",
                  "string"
                ],
                "format": "date-time"
              }
            }
          },
          "new_enum_value": {
            "type": [
              "null",
              "object"
            ],
            "additionalProperties": false,
            "properties": {
              "gid": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "resource_type": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "color": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "enabled": {
                "type": [
                  "null",
                  "boolean"
                ]
              },
              "name": {
                "type": [
                  "null",
                  "string"
                ]
              }
            }
          },
          "new_name": {
            "type": [
              "null",
              "string"
            ]
          },
          "new_number_value": {
            "type": [
              "null",
              "number"
            ]
          },
          "new_resource_subtype": {
            "type": [
              "null",
              "string"
            ]
          },
          "new_section": {
            "type": [
              "null",
              "object"
            ],
            "additionalProperties": false,
            "properties": {
              "gid": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "resource_type": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "name": {
                "type": [
                  "null",
                  "string"
                ]
              }
            }
          },
          "new_text_value": {
            "type": [
              "null",
              "string"
            ]
          },
          "num_hearts": {
            "type": [
              "null",
              "integer"
            ]
          },
          "num_likes": {
            "type": [
              "null",
              "integer"
            ]
          },
          "old_approval_status": {
            "type": [
              "null",
              "string"
            ]
          },
          "old_dates": {
            "type": [
              "null",
              "object"
            ],
            "additionalProperties": false,
            "properties": {
              "due_at": {
                "type": [
                  "null",
                  "string"
                ],
                "format": "date-time"
              },
              "due_on": {
                "type": [
                  "null",
                  "string"
                ],
                "format": "date-time"
              },
              "start_on": {
                "type": [
                  "null",
                  "string"
                ],
                "format": "date-time"
              }
            }
          },
          "old_enum_value": {
            "type": [
              "null",
              "object"
            ],
            "additionalProperties": false,
            "properties": {
              "gid": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "resource_type": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "color": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "enabled": {
                "type": [
                  "null",
                  "boolean"
                ]
              },
              "name": {
                "type": [
                  "null",
                  "string"
                ]
              }
            }
          },
          "old_name": {
            "type": [
              "null",
              "string"
            ]
          },
          "old_number_value": {
            "type": [
              "null",
              "number"
            ]
          },
          "old_resource_subtype": {
            "type": [
              "null",
              "string"
            ]
          },
          "old_section": {
            "type": [
              "null",
              "object"
            ],
            "additionalProperties": false,
            "properties": {
              "gid": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "resource_type": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "name": {
                "type": [
                  "null",
                  "string"
                ]
              }
            }
          },
          "old_text_value": {
            "type": [
              "null",
              "string"
            ]
          },
          "previews": {
            "anyOf": [
              {
                "type": "array",
                "items": {
                  "type": [
                    "null",
                    "object"
                  ],
                  "additionalProperties": false,
                  "properties": {
                    "fallback": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "footer": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "header": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "header_link": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "html_text": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "text": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "title": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "title_link": {
                      "type": [
                        "null",
                        "string"
                      ]
                    }
                  }
                }
              },
              {
                "type": "null"
              }
            ]
          },
          "project": {
            "type": [
              "null",
              "object"
            ],
            "additionalProperties": false,
            "properties": {
              "gid": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "resource_type": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "name": {
                "type": [
                  "null",
                  "string"
                ]
              }
            }
          },
          "source": {
            "type": [
              "null",
              "string"
            ]
          },
          "story": {
            "type": [
              "null",
              "object"
            ],
            "additionalProperties": false,
            "properties": {
              "gid": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "resource_type": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "created_at": {
                "type": [
                  "null",
                  "string"
                ],
                "format": "date-time"
              },
              "created_by": {
                "type": [
                  "null",
                  "object"
                ],
                "additionalProperties": false,
                "properties": {
                  "gid": {
                    "type": [
                      "null",
                      "string"
                    ]
                  },
                  "resource_type": {
                    "type": [
                      "null",
                      "string"
                    ]
                  },
                  "name": {
                    "type": [
                      "null",
                      "string"
                    ]
                  }
                }
              },
              "resource_subtype": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "name": {
                "type": [
                  "null",
                  "string"
                ]
              }
            }
          },
          "tag": {
            "type": [
              "null",
              "object"
            ],
            "additionalProperties": false,
            "properties": {
              "gid": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "resource_type": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "name": {
                "type": [
                  "null",
                  "string"
                ]
              }
            }
          },
          "target": {
            "type": [
              "null",
              "object"
            ],
            "additionalProperties": false,
            "properties": {
              "gid": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "name": {
                "type": [
                  "null",
                  "string"
                ]
              }
            }
          },
          "task": {
            "type": [
              "null",
              "object"
            ],
            "additionalProperties": false,
            "properties": {
              "gid": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "resource_type": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "name": {
                "type": [
                  "null",
                  "string"
                ]
              }
            }
          }
        }
      },
      "metadata": [
        {
          "breadcrumb": [],
          "metadata": {
            "table-key-properties": [
              "gid"
            ],
            "forced-replication-method": "INCREMENTAL",
            "valid-replication-keys": [
              "created_at"
            ],
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "gid"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "resource_type"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "created_at"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "created_by"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "resource_subtype"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "text"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "html_text"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "is_pinned"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "assignee"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "dependency"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "duplicate_of"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "duplicated_from"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "follower"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "hearted"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "hearts"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "is_edited"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "liked"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "likes"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "new_approval_status"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "new_dates"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "new_enum_value"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "new_name"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "new_number_value"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "new_resource_subtype"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "new_section"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "new_text_value"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "num_hearts"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "num_likes"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "old_approval_status"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "old_dates"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "old_enum_value"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "old_name"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "old_number_value"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "old_resource_subtype"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "old_section"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "old_text_value"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "previews"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "project"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "source"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "story"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "tag"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "target"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "task"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        }
      ],
      "key_properties": [
        "gid"
      ],
      "replication_key": "created_at",
      "replication_method": "INCREMENTAL"
    }"""
asana_users="""{
      "type": "SCHEMA",
      "stream": "users",
      "tap_stream_id": "users",
      "schema": {
        "type": [
          "null",
          "object"
        ],
        "additionalProperties": false,
        "properties": {
          "gid": {
            "type": [
              "null",
              "string"
            ]
          },
          "resource_type": {
            "type": [
              "null",
              "string"
            ]
          },
          "name": {
            "type": [
              "null",
              "string"
            ]
          },
          "email": {
            "type": [
              "null",
              "string"
            ]
          },
          "photo": {
            "type": [
              "null",
              "object"
            ],
            "additionalProperties": false,
            "properties": {
              "image_21x21": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "image_27x27": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "image_36x36": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "image_60x60": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "image_128x128": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "image_1024x1024": {
                "type": [
                  "null",
                  "string"
                ]
              }
            }
          },
          "workspaces": {
            "type": [
              "null",
              "array"
            ],
            "items": {
              "type": [
                "null",
                "object"
              ],
              "additionalProperties": false,
              "properties": {
                "gid": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "resource_type": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "name": {
                  "type": [
                    "null",
                    "string"
                  ]
                }
              }
            }
          }
        }
      },
      "metadata": [
        {
          "breadcrumb": [],
          "metadata": {
            "table-key-properties": [
              "gid"
            ],
            "forced-replication-method": "FULL_TABLE",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "gid"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "resource_type"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "name"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "email"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "photo"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "workspaces"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        }
      ],
      "key_properties": [
        "gid"
      ],
      "replication_key": null,
      "replication_method": "FULL_TABLE"
    }"""
asana_workspaces="""{
      "type": "SCHEMA",
      "stream": "workspaces",
      "tap_stream_id": "workspaces",
      "schema": {
        "type": [
          "null",
          "object"
        ],
        "properties": {
          "gid": {
            "type": [
              "null",
              "string"
            ]
          },
          "name": {
            "type": [
              "null",
              "string"
            ]
          },
          "is_organization": {
            "type": [
              "null",
              "boolean"
            ]
          },
          "resource_type": {
            "type": [
              "null",
              "string"
            ]
          },
          "email_domains": {
            "anyOf": [
              {
                "type": "array",
                "items": {
                  "type": "string"
                }
              },
              {
                "type": "null"
              }
            ]
          }
        }
      },
      "metadata": [
        {
          "breadcrumb": [],
          "metadata": {
            "table-key-properties": [
              "gid"
            ],
            "forced-replication-method": "FULL_TABLE",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "gid"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "name"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "is_organization"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "resource_type"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "email_domains"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        }
      ],
      "key_properties": [
        "gid"
      ],
      "replication_key": null,
      "replication_method": "FULL_TABLE"
    }"""

asana_projects="""{
      "type": "SCHEMA",
      "stream": "projects",
      "tap_stream_id": "projects",
      "schema": {
        "type": [
          "null",
          "object"
        ],
        "additionalProperties": false,
        "properties": {
          "name": {
            "type": [
              "null",
              "string"
            ]
          },
          "gid": {
            "type": [
              "null",
              "string"
            ]
          },
          "resource_type": {
            "type": [
              "null",
              "string"
            ]
          },
          "owner": {
            "type": [
              "null",
              "object"
            ],
            "additionalProperties": false,
            "properties": {
              "gid": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "resource_type": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "name": {
                "type": [
                  "null",
                  "string"
                ]
              }
            }
          },
          "current_status": {
            "type": [
              "null",
              "string"
            ]
          },
          "custom_fields": {
            "type": [
              "null",
              "array"
            ],
            "items": {
              "type": [
                "object"
              ],
              "additionalProperties": false,
              "properties": {
                "gid": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "resource_type": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "name": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "resource_subtype": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "type": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "enum_options": {
                  "type": [
                    "null",
                    "array"
                  ],
                  "items": {
                    "type": [
                      "object"
                    ],
                    "additionalProperties": false,
                    "properties": {
                      "gid": {
                        "type": [
                          "null",
                          "string"
                        ]
                      },
                      "resource_type": {
                        "type": [
                          "null",
                          "string"
                        ]
                      },
                      "name": {
                        "type": [
                          "null",
                          "string"
                        ]
                      },
                      "enabled": {
                        "type": [
                          "null",
                          "boolean"
                        ]
                      },
                      "color": {
                        "type": [
                          "null",
                          "string"
                        ]
                      }
                    }
                  }
                },
                "enum_value": {
                  "type": [
                    "null",
                    "object"
                  ],
                  "additionalProperties": false,
                  "properties": {
                    "gid": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "resource_type": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "name": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "enabled": {
                      "type": [
                        "null",
                        "boolean"
                      ]
                    },
                    "color": {
                      "type": [
                        "null",
                        "string"
                      ]
                    }
                  }
                },
                "enabled": {
                  "type": [
                    "null",
                    "boolean"
                  ]
                },
                "text_value": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "number_value": {
                  "type": [
                    "null",
                    "number"
                  ]
                },
                "description": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "precision": {
                  "type": [
                    "null",
                    "integer"
                  ]
                },
                "is_global_to_workspace": {
                  "type": [
                    "null",
                    "boolean"
                  ]
                },
                "has_notifications_enabled": {
                  "type": [
                    "null",
                    "boolean"
                  ]
                }
              }
            }
          },
          "default_view": {
            "type": [
              "null",
              "string"
            ]
          },
          "due_date": {
            "type": [
              "null",
              "string"
            ]
          },
          "due_on": {
            "type": [
              "null",
              "string"
            ]
          },
          "html_notes": {
            "type": [
              "null",
              "string"
            ]
          },
          "is_template": {
            "type": [
              "null",
              "boolean"
            ]
          },
          "created_at": {
            "type": [
              "null",
              "string"
            ],
            "format": "date-time"
          },
          "modified_at": {
            "type": [
              "null",
              "string"
            ],
            "format": "date-time"
          },
          "start_on": {
            "type": [
              "null",
              "string"
            ]
          },
          "archived": {
            "type": [
              "null",
              "boolean"
            ]
          },
          "public": {
            "type": [
              "null",
              "boolean"
            ]
          },
          "members": {
            "type": [
              "null",
              "array"
            ],
            "items": {
              "type": [
                "null",
                "object"
              ],
              "additionalProperties": false,
              "properties": {
                "gid": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "resource_type": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "name": {
                  "type": [
                    "null",
                    "string"
                  ]
                }
              }
            }
          },
          "followers": {
            "type": [
              "null",
              "array"
            ],
            "items": {
              "type": [
                "null",
                "object"
              ],
              "additionalProperties": false,
              "properties": {
                "gid": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "resource_type": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "name": {
                  "type": [
                    "null",
                    "string"
                  ]
                }
              }
            }
          },
          "color": {
            "type": [
              "null",
              "string"
            ]
          },
          "notes": {
            "type": [
              "null",
              "string"
            ]
          },
          "icon": {
            "type": [
              "null",
              "string"
            ]
          },
          "permalink_url": {
            "type": [
              "null",
              "string"
            ]
          },
          "workspace": {
            "type": [
              "null",
              "object"
            ],
            "additionalProperties": false,
            "properties": {
              "gid": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "resource_type": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "name": {
                "type": [
                  "null",
                  "string"
                ]
              }
            }
          },
          "team": {
            "type": [
              "null",
              "object"
            ],
            "additionalProperties": false,
            "properties": {
              "gid": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "resource_type": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "name": {
                "type": [
                  "null",
                  "string"
                ]
              }
            }
          }
        }
      },
      "metadata": [
        {
          "breadcrumb": [],
          "metadata": {
            "table-key-properties": [
              "gid"
            ],
            "forced-replication-method": "INCREMENTAL",
            "valid-replication-keys": [
              "modified_at"
            ],
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "name"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "gid"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "resource_type"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "owner"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "current_status"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "custom_fields"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "default_view"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "due_date"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "due_on"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "html_notes"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "is_template"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "created_at"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "modified_at"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "start_on"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "archived"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "public"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "members"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "followers"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "color"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "notes"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "icon"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "permalink_url"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "workspace"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "team"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        }
      ],
      "key_properties": [
        "gid"
      ],
      "replication_key": "modified_at",
      "replication_method": "INCREMENTAL"
    }"""
asana_portfolios = """{
      "type": "SCHEMA",
      "stream": "portfolios",
      "tap_stream_id": "portfolios",
      "schema": {
        "type": [
          "null",
          "object"
        ],
        "additionalProperties": false,
        "properties": {
          "gid": {
            "type": [
              "null",
              "string"
            ]
          },
          "resource_type": {
            "type": [
              "null",
              "string"
            ]
          },
          "name": {
            "type": [
              "null",
              "string"
            ]
          },
          "color": {
            "type": [
              "null",
              "string"
            ]
          },
          "created_at": {
            "type": [
              "null",
              "string"
            ],
            "format": "date-time"
          },
          "created_by": {
            "type": [
              "null",
              "object"
            ],
            "additionalProperties": false,
            "properties": {
              "gid": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "resource_type": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "name": {
                "type": [
                  "null",
                  "string"
                ]
              }
            }
          },
          "custom_field_settings": {
            "type": [
              "null",
              "array"
            ],
            "items": {
              "type": [
                "object"
              ],
              "additionalProperties": false,
              "properties": {
                "gid": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "resource_type": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "custom_field": {
                  "type": [
                    "null",
                    "object"
                  ],
                  "additionalProperties": false,
                  "properties": {
                    "gid": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "resource_type": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "currency_code": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "custom_label": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "custom_label_position": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "description": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "enabled": {
                      "type": [
                        "null",
                        "boolean"
                      ]
                    },
                    "enum_options": {
                      "type": [
                        "null",
                        "array"
                      ],
                      "items": {
                        "type": [
                          "object"
                        ],
                        "additionalProperties": false,
                        "properties": {
                          "gid": {
                            "type": [
                              "null",
                              "string"
                            ]
                          },
                          "resource_type": {
                            "type": [
                              "null",
                              "string"
                            ]
                          },
                          "name": {
                            "type": [
                              "null",
                              "string"
                            ]
                          },
                          "enabled": {
                            "type": [
                              "null",
                              "boolean"
                            ]
                          },
                          "color": {
                            "type": [
                              "null",
                              "string"
                            ]
                          }
                        }
                      }
                    },
                    "enum_value": {
                      "type": [
                        "null",
                        "object"
                      ],
                      "additionalProperties": false,
                      "properties": {
                        "gid": {
                          "type": [
                            "null",
                            "string"
                          ]
                        },
                        "resource_type": {
                          "type": [
                            "null",
                            "string"
                          ]
                        },
                        "name": {
                          "type": [
                            "null",
                            "string"
                          ]
                        },
                        "enabled": {
                          "type": [
                            "null",
                            "boolean"
                          ]
                        },
                        "color": {
                          "type": [
                            "null",
                            "string"
                          ]
                        }
                      }
                    },
                    "format": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "has_notifications_enabled": {
                      "type": [
                        "null",
                        "boolean"
                      ]
                    },
                    "is_global_to_workspace": {
                      "type": [
                        "null",
                        "boolean"
                      ]
                    },
                    "name": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "number_value": {
                      "type": [
                        "null",
                        "number"
                      ]
                    },
                    "precision": {
                      "type": [
                        "null",
                        "integer"
                      ]
                    },
                    "resource_subtype": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "text_value": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "type": {
                      "type": [
                        "null",
                        "string"
                      ]
                    }
                  }
                },
                "is_important": {
                  "type": [
                    "null",
                    "boolean"
                  ]
                },
                "parent": {
                  "type": [
                    "null",
                    "object"
                  ],
                  "additionalProperties": false,
                  "properties": {
                    "gid": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "resource_type": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "name": {
                      "type": [
                        "null",
                        "string"
                      ]
                    }
                  }
                },
                "project": {
                  "type": [
                    "null",
                    "object"
                  ],
                  "additionalProperties": false,
                  "properties": {
                    "gid": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "resource_type": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "name": {
                      "type": [
                        "null",
                        "string"
                      ]
                    }
                  }
                }
              }
            }
          },
          "is_template": {
            "type": [
              "null",
              "boolean"
            ]
          },
          "due_on": {
            "type": [
              "null",
              "string"
            ]
          },
          "members": {
            "type": [
              "null",
              "array"
            ],
            "items": {
              "type": [
                "null",
                "object"
              ],
              "additionalProperties": false,
              "properties": {
                "gid": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "resource_type": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "name": {
                  "type": [
                    "null",
                    "string"
                  ]
                }
              }
            }
          },
          "owner": {
            "type": [
              "null",
              "object"
            ],
            "additionalProperties": false,
            "properties": {
              "gid": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "resource_type": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "name": {
                "type": [
                  "null",
                  "string"
                ]
              }
            }
          },
          "permalink_url": {
            "type": [
              "null",
              "string"
            ]
          },
          "start_on": {
            "type": [
              "null",
              "string"
            ]
          },
          "workspace": {
            "type": [
              "null",
              "object"
            ],
            "additionalProperties": false,
            "properties": {
              "gid": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "resource_type": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "name": {
                "type": [
                  "null",
                  "string"
                ]
              }
            }
          },
          "portfolio_items": {
            "type": [
              "null",
              "array"
            ],
            "items": {
              "type": [
                "null",
                "object"
              ],
              "additionalProperties": false,
              "properties": {
                "gid": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "resource_type": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "name": {
                  "type": [
                    "null",
                    "string"
                  ]
                }
              }
            }
          }
        }
      },
      "metadata": [
        {
          "breadcrumb": [],
          "metadata": {
            "table-key-properties": [
              "gid"
            ],
            "forced-replication-method": "FULL_TABLE",
            "selected": false
          }
        },
        {
          "breadcrumb": [
            "properties",
            "gid"
          ],
          "metadata": {
            "inclusion": "automatic"
          }
        },
        {
          "breadcrumb": [
            "properties",
            "resource_type"
          ],
          "metadata": {
            "inclusion": "available"
          }
        },
        {
          "breadcrumb": [
            "properties",
            "name"
          ],
          "metadata": {
            "inclusion": "available"
          }
        },
        {
          "breadcrumb": [
            "properties",
            "color"
          ],
          "metadata": {
            "inclusion": "available"
          }
        },
        {
          "breadcrumb": [
            "properties",
            "created_at"
          ],
          "metadata": {
            "inclusion": "available"
          }
        },
        {
          "breadcrumb": [
            "properties",
            "created_by"
          ],
          "metadata": {
            "inclusion": "available"
          }
        },
        {
          "breadcrumb": [
            "properties",
            "custom_field_settings"
          ],
          "metadata": {
            "inclusion": "available"
          }
        },
        {
          "breadcrumb": [
            "properties",
            "is_template"
          ],
          "metadata": {
            "inclusion": "available"
          }
        },
        {
          "breadcrumb": [
            "properties",
            "due_on"
          ],
          "metadata": {
            "inclusion": "available"
          }
        },
        {
          "breadcrumb": [
            "properties",
            "members"
          ],
          "metadata": {
            "inclusion": "available"
          }
        },
        {
          "breadcrumb": [
            "properties",
            "owner"
          ],
          "metadata": {
            "inclusion": "available"
          }
        },
        {
          "breadcrumb": [
            "properties",
            "permalink_url"
          ],
          "metadata": {
            "inclusion": "available"
          }
        },
        {
          "breadcrumb": [
            "properties",
            "start_on"
          ],
          "metadata": {
            "inclusion": "available"
          }
        },
        {
          "breadcrumb": [
            "properties",
            "workspace"
          ],
          "metadata": {
            "inclusion": "available"
          }
        },
        {
          "breadcrumb": [
            "properties",
            "portfolio_items"
          ],
          "metadata": {
            "inclusion": "available"
          }
        }
      ],
      "key_properties": [
        "gid"
      ],
      "replication_key": null,
      "replication_method": "FULL_TABLE"
    }"""
asana_sections="""{
      "type": "SCHEMA",
      "stream": "sections",
      "tap_stream_id": "sections",
      "schema": {
        "type": [
          "null",
          "object"
        ],
        "additionalProperties": false,
        "properties": {
          "gid": {
            "type": [
              "null",
              "string"
            ]
          },
          "resource_type": {
            "type": [
              "null",
              "string"
            ]
          },
          "name": {
            "type": [
              "null",
              "string"
            ]
          },
          "created_at": {
            "type": [
              "null",
              "string"
            ],
            "format": "date-time"
          },
          "project": {
            "type": [
              "null",
              "object"
            ],
            "additionalProperties": false,
            "properties": {
              "gid": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "resource_type": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "name": {
                "type": [
                  "null",
                  "string"
                ]
              }
            }
          },
          "projects": {
            "type": [
              "null",
              "array"
            ],
            "items": {
              "type": [
                "null",
                "object"
              ],
              "additionalProperties": false,
              "properties": {
                "gid": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "resource_type": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "name": {
                  "type": [
                    "null",
                    "string"
                  ]
                }
              }
            }
          }
        }
      },
      "metadata": [
        {
          "breadcrumb": [],
          "metadata": {
            "table-key-properties": [
              "gid"
            ],
            "forced-replication-method": "FULL_TABLE",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "gid"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "resource_type"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "name"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "created_at"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "project"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "projects"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        }
      ],
      "key_properties": [
        "gid"
      ],
      "replication_key": null,
      "replication_method": "FULL_TABLE"
    }"""
asana_tasks="""{
      "type": "SCHEMA",
      "stream": "tasks",
      "tap_stream_id": "tasks",
      "schema": {
        "type": [
          "null",
          "object"
        ],
        "additionalProperties": false,
        "properties": {
          "gid": {
            "type": [
              "null",
              "string"
            ]
          },
          "resource_type": {
            "type": [
              "null",
              "string"
            ]
          },
          "name": {
            "type": [
              "null",
              "string"
            ]
          },
          "approval_status": {
            "type": [
              "null",
              "string"
            ]
          },
          "assignee_status": {
            "type": [
              "null",
              "string"
            ]
          },
          "completed": {
            "type": [
              "null",
              "boolean"
            ]
          },
          "completed_at": {
            "type": [
              "null",
              "string"
            ],
            "format": "date-time"
          },
          "completed_by": {
            "type": [
              "null",
              "object"
            ],
            "additionalProperties": false,
            "properties": {
              "gid": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "resource_type": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "name": {
                "type": [
                  "null",
                  "string"
                ]
              }
            }
          },
          "created_at": {
            "type": [
              "null",
              "string"
            ],
            "format": "date-time"
          },
          "dependencies": {
            "type": [
              "null",
              "array"
            ],
            "items": {
              "type": [
                "null",
                "object"
              ],
              "additionalProperties": false,
              "properties": {
                "gid": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "resource_type": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "name": {
                  "type": [
                    "null",
                    "string"
                  ]
                }
              }
            }
          },
          "dependents": {
            "type": [
              "null",
              "array"
            ],
            "items": {
              "type": [
                "null",
                "object"
              ],
              "additionalProperties": false,
              "properties": {
                "gid": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "resource_type": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "name": {
                  "type": [
                    "null",
                    "string"
                  ]
                }
              }
            }
          },
          "due_at": {
            "type": [
              "null",
              "string"
            ],
            "format": "date-time"
          },
          "due_on": {
            "type": [
              "null",
              "string"
            ],
            "format": "date-time"
          },
          "external": {
            "type": [
              "null",
              "object"
            ],
            "additionalProperties": false,
            "properties": {
              "gid": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "data": {
                "type": [
                  "null",
                  "string"
                ]
              }
            }
          },
          "hearted": {
            "type": [
              "null",
              "boolean"
            ]
          },
          "hearts": {
            "anyOf": [
              {
                "type": "array",
                "items": {
                  "type": [
                    "null",
                    "object"
                  ],
                  "additionalProperties": false,
                  "properties": {
                    "gid": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "user": {
                      "type": [
                        "null",
                        "object"
                      ],
                      "additionalProperties": false,
                      "properties": {
                        "gid": {
                          "type": [
                            "null",
                            "string"
                          ]
                        },
                        "resource_type": {
                          "type": [
                            "null",
                            "string"
                          ]
                        },
                        "name": {
                          "type": [
                            "null",
                            "string"
                          ]
                        }
                      }
                    }
                  }
                }
              },
              {
                "type": "null"
              }
            ]
          },
          "html_notes": {
            "type": [
              "null",
              "string"
            ]
          },
          "is_rendered_as_seperator": {
            "type": [
              "null",
              "boolean"
            ]
          },
          "liked": {
            "type": [
              "null",
              "boolean"
            ]
          },
          "likes": {
            "anyOf": [
              {
                "type": "array",
                "items": {
                  "type": [
                    "null",
                    "object"
                  ],
                  "additionalProperties": false,
                  "properties": {
                    "gid": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "user": {
                      "type": [
                        "null",
                        "object"
                      ],
                      "additionalProperties": false,
                      "properties": {
                        "gid": {
                          "type": [
                            "null",
                            "string"
                          ]
                        },
                        "resource_type": {
                          "type": [
                            "null",
                            "string"
                          ]
                        },
                        "name": {
                          "type": [
                            "null",
                            "string"
                          ]
                        }
                      }
                    }
                  }
                }
              },
              {
                "type": "null"
              }
            ]
          },
          "memberships": {
            "anyOf": [
              {
                "type": "array",
                "items": {
                  "type": [
                    "null",
                    "object"
                  ],
                  "additionalProperties": false,
                  "properties": {
                    "project": {
                      "type": [
                        "null",
                        "object"
                      ],
                      "additionalProperties": false,
                      "properties": {
                        "gid": {
                          "type": [
                            "null",
                            "string"
                          ]
                        },
                        "resource_type": {
                          "type": [
                            "null",
                            "string"
                          ]
                        },
                        "name": {
                          "type": [
                            "null",
                            "string"
                          ]
                        }
                      }
                    },
                    "section": {
                      "type": [
                        "null",
                        "object"
                      ],
                      "additionalProperties": false,
                      "properties": {
                        "gid": {
                          "type": [
                            "null",
                            "string"
                          ]
                        },
                        "resource_type": {
                          "type": [
                            "null",
                            "string"
                          ]
                        },
                        "name": {
                          "type": [
                            "null",
                            "string"
                          ]
                        }
                      }
                    }
                  }
                }
              },
              {
                "type": "null"
              }
            ]
          },
          "modified_at": {
            "type": [
              "null",
              "string"
            ],
            "format": "date-time"
          },
          "notes": {
            "type": [
              "null",
              "string"
            ]
          },
          "num_hearts": {
            "type": [
              "null",
              "integer"
            ]
          },
          "num_likes": {
            "type": [
              "null",
              "integer"
            ]
          },
          "num_subtasks": {
            "type": [
              "null",
              "integer"
            ]
          },
          "resource_subtype": {
            "type": [
              "null",
              "string"
            ]
          },
          "start_on": {
            "type": [
              "null",
              "string"
            ]
          },
          "assignee": {
            "type": [
              "null",
              "object"
            ],
            "additionalProperties": false,
            "properties": {
              "gid": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "resource_type": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "name": {
                "type": [
                  "null",
                  "string"
                ]
              }
            }
          },
          "custom_fields": {
            "type": [
              "null",
              "array"
            ],
            "items": {
              "type": [
                "null",
                "object"
              ],
              "additionalProperties": false,
              "properties": {
                "gid": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "resource_type": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "name": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "resource_subtype": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "type": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "enum_options": {
                  "type": [
                    "null",
                    "array"
                  ],
                  "items": {
                    "type": [
                      "null",
                      "object"
                    ],
                    "additionalProperties": false,
                    "properties": {
                      "gid": {
                        "type": [
                          "null",
                          "string"
                        ]
                      },
                      "resource_type": {
                        "type": [
                          "null",
                          "string"
                        ]
                      },
                      "name": {
                        "type": [
                          "null",
                          "string"
                        ]
                      },
                      "enabled": {
                        "type": [
                          "null",
                          "boolean"
                        ]
                      },
                      "color": {
                        "type": [
                          "null",
                          "string"
                        ]
                      }
                    }
                  }
                },
                "enum_value": {
                  "type": [
                    "null",
                    "object"
                  ],
                  "additionalProperties": false,
                  "properties": {
                    "gid": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "resource_type": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "name": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "enabled": {
                      "type": [
                        "null",
                        "boolean"
                      ]
                    },
                    "color": {
                      "type": [
                        "null",
                        "string"
                      ]
                    }
                  }
                },
                "enabled": {
                  "type": [
                    "null",
                    "boolean"
                  ]
                },
                "text_value": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "number_value": {
                  "type": [
                    "null",
                    "number"
                  ]
                },
                "description": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "precision": {
                  "type": [
                    "null",
                    "integer"
                  ]
                },
                "is_global_to_workspace": {
                  "type": [
                    "null",
                    "boolean"
                  ]
                },
                "has_notifications_enabled": {
                  "type": [
                    "null",
                    "boolean"
                  ]
                }
              }
            }
          },
          "followers": {
            "type": [
              "null",
              "array"
            ],
            "items": {
              "type": [
                "null",
                "object"
              ],
              "additionalProperties": false,
              "properties": {
                "gid": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "resource_type": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "name": {
                  "type": [
                    "null",
                    "string"
                  ]
                }
              }
            }
          },
          "parent": {
            "type": [
              "null",
              "object"
            ],
            "additionalProperties": false,
            "properties": {
              "gid": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "resource_type": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "name": {
                "type": [
                  "null",
                  "string"
                ]
              }
            }
          },
          "permalink_url": {
            "type": [
              "null",
              "string"
            ]
          },
          "projects": {
            "type": [
              "null",
              "array"
            ],
            "items": {
              "type": [
                "null",
                "object"
              ],
              "additionalProperties": false,
              "properties": {
                "gid": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "resource_type": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "name": {
                  "type": [
                    "null",
                    "string"
                  ]
                }
              }
            }
          },
          "tags": {
            "type": [
              "null",
              "array"
            ],
            "items": {
              "type": [
                "null",
                "object"
              ],
              "additionalProperties": false,
              "properties": {
                "gid": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "resource_type": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "name": {
                  "type": [
                    "null",
                    "string"
                  ]
                }
              }
            }
          },
          "workspace": {
            "type": [
              "null",
              "object"
            ],
            "additionalProperties": false,
            "properties": {
              "gid": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "resource_type": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "name": {
                "type": [
                  "null",
                  "string"
                ]
              }
            }
          }
        }
      },
      "metadata": [
        {
          "breadcrumb": [],
          "metadata": {
            "table-key-properties": [
              "gid"
            ],
            "forced-replication-method": "INCREMENTAL",
            "valid-replication-keys": [
              "modified_at"
            ],
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "gid"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "resource_type"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "name"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "approval_status"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "assignee_status"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "completed"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "completed_at"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "completed_by"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "created_at"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "dependencies"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "dependents"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "due_at"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "due_on"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "external"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "hearted"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "hearts"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "html_notes"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "is_rendered_as_seperator"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "liked"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "likes"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "memberships"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "modified_at"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "notes"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "num_hearts"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "num_likes"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "num_subtasks"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "resource_subtype"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "start_on"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "assignee"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "custom_fields"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "followers"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "parent"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "permalink_url"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "projects"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "tags"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "workspace"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        }
      ],
      "key_properties": [
        "gid"
      ],
      "replication_key": "modified_at",
      "replication_method": "INCREMENTAL"
    }"""
asana_tags="""{
      "type": "SCHEMA",
      "stream": "tags",
      "tap_stream_id": "tags",
      "schema": {
        "type": [
          "null",
          "object"
        ],
        "additionalProperties": false,
        "properties": {
          "gid": {
            "type": [
              "null",
              "string"
            ]
          },
          "resource_type": {
            "type": [
              "null",
              "string"
            ]
          },
          "created_at": {
            "type": [
              "null",
              "string"
            ],
            "format": "date-time"
          },
          "followers": {
            "type": [
              "null",
              "array"
            ],
            "items": {
              "type": [
                "null",
                "object"
              ],
              "additionalProperties": false,
              "properties": {
                "gid": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "resource_type": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "name": {
                  "type": [
                    "null",
                    "string"
                  ]
                }
              }
            }
          },
          "name": {
            "type": [
              "null",
              "string"
            ]
          },
          "color": {
            "type": [
              "null",
              "string"
            ]
          },
          "notes": {
            "type": [
              "null",
              "string"
            ]
          },
          "permalink_url": {
            "type": [
              "null",
              "string"
            ]
          },
          "workspace": {
            "type": [
              "null",
              "object"
            ],
            "additionalProperties": false,
            "properties": {
              "gid": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "resource_type": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "name": {
                "type": [
                  "null",
                  "string"
                ]
              }
            }
          }
        }
      },
      "metadata": [
        {
          "breadcrumb": [],
          "metadata": {
            "table-key-properties": [
              "gid"
            ],
            "forced-replication-method": "INCREMENTAL",
            "valid-replication-keys": [
              "created_at"
            ],
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "gid"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "resource_type"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "created_at"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "followers"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "name"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "color"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "notes"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "permalink_url"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "workspace"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        }
      ],
      "key_properties": [
        "gid"
      ],
      "replication_key": "created_at",
      "replication_method": "INCREMENTAL"
    }"""