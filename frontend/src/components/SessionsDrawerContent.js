import React, { useState } from 'react';
import { StyleSheet, View, Text, TouchableOpacity, FlatList } from 'react-native';
import { DrawerContentScrollView } from '@react-navigation/drawer';
import { Ionicons } from '@expo/vector-icons';

const SessionsDrawerContent = (props) => {
  // Placeholder data for chat sessions
  const [sessions, setSessions] = useState([
    { id: '1', title: 'Yellow leaves on tomato plant', date: '2 hours ago' },
    { id: '2', title: 'Soil pH for blueberries', date: '1 day ago' },
    { id: '3', title: 'Sustainable farming practices', date: '3 days ago' },
    { id: '4', title: 'Identifying a wildflower', date: '1 week ago' },
  ]);

  const renderSessionItem = ({ item }) => (
    <TouchableOpacity 
      style={styles.sessionItem}
      onPress={() => {
        // In the future, this would load the specific chat session
        props.navigation.navigate('Chat');
        props.navigation.closeDrawer();
      }}
    >
      <Ionicons name="chatbubble-ellipses-outline" size={20} color="#2e7d32" style={styles.sessionIcon} />
      <View style={styles.sessionInfo}>
        <Text style={styles.sessionTitle} numberOfLines={1}>{item.title}</Text>
        <Text style={styles.sessionDate}>{item.date}</Text>
      </View>
    </TouchableOpacity>
  );

  return (
    <DrawerContentScrollView {...props} style={styles.container}>
      <View style={styles.header}>
        <Text style={styles.headerTitle}>Chat Sessions</Text>
      </View>
      
      <TouchableOpacity 
        style={styles.newChatButton}
        onPress={() => {
          props.navigation.navigate('Chat');
          props.navigation.closeDrawer();
        }}
      >
        <Ionicons name="add-circle" size={20} color="#fff" />
        <Text style={styles.newChatButtonText}>New Chat</Text>
      </TouchableOpacity>
      
      <FlatList
        data={sessions}
        renderItem={renderSessionItem}
        keyExtractor={item => item.id}
        style={styles.sessionsList}
      />
      
      <View style={styles.footer}>
        <TouchableOpacity 
          style={styles.footerButton}
          onPress={() => props.navigation.navigate('Dashboard')}
        >
          <Ionicons name="stats-chart" size={20} color="#2e7d32" />
          <Text style={styles.footerButtonText}>Dashboard</Text>
        </TouchableOpacity>
      </View>
    </DrawerContentScrollView>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#f5f5f5',
  },
  header: {
    padding: 16,
    borderBottomWidth: 1,
    borderBottomColor: '#e0e0e0',
    backgroundColor: '#2e7d32',
  },
  headerTitle: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#fff',
  },
  newChatButton: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: '#2e7d32',
    padding: 12,
    margin: 16,
    borderRadius: 8,
    justifyContent: 'center',
  },
  newChatButtonText: {
    color: '#fff',
    fontWeight: '600',
    marginLeft: 8,
  },
  sessionsList: {
    flex: 1,
    marginTop: 8,
  },
  sessionItem: {
    flexDirection: 'row',
    alignItems: 'center',
    padding: 16,
    borderBottomWidth: 1,
    borderBottomColor: '#e0e0e0',
  },
  sessionIcon: {
    marginRight: 12,
  },
  sessionInfo: {
    flex: 1,
  },
  sessionTitle: {
    fontSize: 14,
    fontWeight: '500',
    color: '#333',
    marginBottom: 4,
  },
  sessionDate: {
    fontSize: 12,
    color: '#888',
  },
  footer: {
    padding: 16,
    borderTopWidth: 1,
    borderTopColor: '#e0e0e0',
  },
  footerButton: {
    flexDirection: 'row',
    alignItems: 'center',
  },
  footerButtonText: {
    color: '#2e7d32',
    fontWeight: '500',
    marginLeft: 8,
  },
});

export default SessionsDrawerContent;